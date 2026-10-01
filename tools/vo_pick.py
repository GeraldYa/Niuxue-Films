"""配音每句多种子挑一版：同一个音色、同一句话，换种子配出来的吐字好坏差不少。每句配几个种子（白板工具：SEED_OFFSET=100 FORCE_TTS=1 wb tts <期>），
把每次的 work/audio 拷进各自的候选目录，再用这个脚本逐句打分，留最好的一版，输出目录直接给 tools/vo_import.py 用。
打分（whisper large-v3-turbo 转写，whisper.cpp 的 whisper-cli；模型路径用环境变量 WHISPER_MODEL，默认 ~/.cache/whisper-models/ggml-large-v3-turbo.bin）：
  1) 拼音错字率：转写和台本都转成不带声调的拼音再比（pypinyin），他/它、每/美这类同音字不算错；越低越好 —— 吐字清不清；
  2) 平均字置信度：越高越好；
  3) 吞字重罚：对齐结果里某个字时长不到 30 ms，或者那段最响处比整句最响处低 35 dB 以上，就当这个字没念出来。
     这种句子识别器常常照样「听全」（它会补字），按字算错字率反而最低，所以要单独查；
  4) 句尾截断扣分：最后 10 ms 还在 −30 dB（相对这句最响处）以上，多半是尾音被切了；
  5) 气声扣分：4 kHz 以上对 80 Hz–4 kHz 的能量比，正常 −27 到 −30 dB；超过 −26.5 dB 每 dB 扣 4 分。
     辅音多的句子本来就偏高，几个种子都高的话不用硬挑。
依赖：仓库的 .venv 之外还要 pypinyin（uv pip install --python .venv/bin/python pypinyin）。
用法：.venv/bin/python tools/vo_pick.py <scenes.js> <输出目录> <候选目录>...
  scenes.js 里每句写成 ['L01', '台词'] 的样子；候选目录里是每句一对 Lxx.wav + Lxx.json（wordList 逐字时间）。
输出目录里放每句选中的 Lxx.wav + Lxx.json，外加 挑句结果.md；whisper 结果缓存在输出目录的 asr缓存.json。"""
import sys, os, re, json, shutil, subprocess, tempfile, unicodedata
import numpy as np, soundfile as sf
M = os.path.expanduser(os.environ.get('WHISPER_MODEL', '~/.cache/whisper-models/ggml-large-v3-turbo.bin'))
han = lambda s: [c for c in s if unicodedata.category(c).startswith('L') or c.isdigit()]
def cer(ref, hyp):
    r, h = han(ref), han(hyp); d = list(range(len(h) + 1))
    for i in range(1, len(r) + 1):
        p, d[0] = d[0], i
        for j in range(1, len(h) + 1): p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (r[i - 1] != h[j - 1]))
    return d[len(h)] / max(1, len(r))
from pypinyin import lazy_pinyin
def pcer(ref, hyp):
    r, h = lazy_pinyin(''.join(han(ref))), lazy_pinyin(''.join(han(hyp))); d = list(range(len(h) + 1))
    for i in range(1, len(r) + 1):
        p, d[0] = d[0], i
        for j in range(1, len(h) + 1): p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (r[i - 1] != h[j - 1]))
    return d[len(h)] / max(1, len(r))
def swallowed(wav, js):
    y, sr = sf.read(wav); y = y.mean(1) if y.ndim > 1 else y; mx = np.abs(y).max() + 1e-12; n = 0
    for u in json.load(open(js, encoding='utf-8'))['wordList']:
        k = len(han(u['w']))
        if not k: continue
        a, b = int(u['s'] * sr), int(u['e'] * sr)
        if u['e'] - u['s'] < .03 or b <= a or 20 * np.log10(np.abs(y[a:b]).max() / mx + 1e-12) < -35: n += k
    return n
CACHE = {}
def asr(wav):
    key = f'{os.path.abspath(wav)}|{os.path.getmtime(wav)}'
    if key in CACHE: return tuple(CACHE[key])
    r = _asr(wav); CACHE[key] = list(r); return r
def _asr(wav):
    with tempfile.TemporaryDirectory() as td:
        w16 = os.path.join(td, 'a.wav'); subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', wav, '-ar', '16000', '-ac', '1', w16], check=True)
        subprocess.run(['whisper-cli', '-m', M, '-l', 'zh', '-f', w16, '-ojf', '-of', os.path.join(td, 'o'), '-np'], check=True, capture_output=True)
        J = json.load(open(os.path.join(td, 'o.json')))
    hyp = ''.join(s['text'] for s in J['transcription'])
    ps = [t['p'] for s in J['transcription'] for t in s.get('tokens', []) if not t['text'].startswith('[') and han(t['text'])]
    return hyp.strip(), (sum(ps) / len(ps) if ps else 0.)
def breath_db(wav):
    from scipy.signal import welch
    y, sr = sf.read(wav); y = y.mean(1) if y.ndim > 1 else y; f, P = welch(y, sr, nperseg=4096)
    return float(10 * np.log10(P[f >= 4000].sum() / P[(f >= 80) & (f < 4000)].sum()))
def tail_db(wav):
    y, sr = sf.read(wav); y = y.mean(1) if y.ndim > 1 else y; w = int(.01 * sr)
    e = np.array([np.sqrt(np.mean(y[i:i + w] ** 2)) for i in range(0, len(y) - w + 1, w)]); return float(20 * np.log10(e[-1] / (e.max() + 1e-12) + 1e-9))
src, out, cands = sys.argv[1], sys.argv[2], sys.argv[3:]
TEXT = dict(re.findall(r"\['(L\d\d)',\s*'([^']*)'\]", open(src, encoding='utf-8').read()))
os.makedirs(out, exist_ok=True); CF = os.path.join(out, 'asr缓存.json')
if os.path.exists(CF): CACHE.update(json.load(open(CF, encoding='utf-8')))
rep = ['# 挑句结果', '', '| 句 | ' + ' | '.join(os.path.basename(c.rstrip('/')) for c in cands) + ' | 选 |', '|---|' + '---|' * (len(cands) + 1)]
tot = {c: [] for c in cands}
for k, ref in TEXT.items():
    rows = []
    for c in cands:
        wav = os.path.join(c, k + '.wav')
        if not os.path.exists(wav): rows.append(None); continue
        hyp, p = asr(wav); e = pcer(ref, hyp); td = tail_db(wav); cut = td > -30; sw = swallowed(wav, os.path.join(c, k + '.json')); br = breath_db(wav)
        score = e * 100 + (1 - p) * 10 + (5 if cut else 0) + 30 * sw + 4 * max(0., br + 26.5); rows.append((score, e, p, td, cut, hyp, sw, br)); tot[c].append((e, p, cut, sw))
    best = min((i for i, r in enumerate(rows) if r), key=lambda i: rows[i][0])
    for ext in ('.wav', '.json'): shutil.copy2(os.path.join(cands[best], k + ext), os.path.join(out, k + ext))
    cell = lambda r: '—' if not r else f"{r[1] * 100:.0f}% · {r[2]:.3f}{' · 尾截' if r[4] else ''}{f' · 吞{r[6]}字' if r[6] else ''} · 气{r[7]:.0f}"
    rep.append(f'| {k} | ' + ' | '.join(cell(r) for r in rows) + f' | {os.path.basename(cands[best].rstrip("/"))} |')
    print(k, ' | '.join(cell(r) for r in rows), '→', os.path.basename(cands[best].rstrip('/')), flush=True)
json.dump(CACHE, open(CF, 'w', encoding='utf-8'), ensure_ascii=False)
rep += ['', '每格：拼音错字率 · 平均字置信度（· 尾截 = 句尾像被切了；· 吞 N 字 = 对齐出来没声音的字）。分数 = 拼音错字率×100 + (1−置信度)×10 + 尾截 5 + 吞字 30/字 + 气声比超过 −26.5 dB 每 dB 4 分，取最小。· 气 N = 气声比（dB）。', '']
for c in cands:
    v = tot[c]; rep.append(f'- {os.path.basename(c.rstrip("/"))}：平均拼音错字率 {np.mean([x[0] for x in v]) * 100:.1f}%，平均置信度 {np.mean([x[1] for x in v]):.3f}，尾截 {sum(x[2] for x in v)} 句，吞字 {sum(x[3] for x in v)} 个')
open(os.path.join(out, '挑句结果.md'), 'w').write('\n'.join(rep) + '\n'); print('\n'.join(rep[-len(cands):]))
