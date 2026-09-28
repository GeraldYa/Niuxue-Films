"""把白板工具（台式机 VoxCPM2）配好的句子导进片子：拷 WAV、生成 words.json，可选压长停顿。

用法（仓库根）：
  .venv/bin/python tools/vo_import.py <wb 期的 work/audio 目录> films/<名>/voices [--tighten 0.45] [--only L07,L08]

输入：目录里每句一对 Lxx.wav + Lxx.json（wordList: [{w, s, e}], duration）。
输出：<voices>/Lxx.wav，以及 <voices>/words.json：{id: {dur, u: [[字, 起, 止], ...]}}。
  已有的 words.json 会保留，同名句子覆盖。
--tighten CAP：句内超过 CAP 秒的停顿压到 CAP。
  只剪连续静音段（RMS < −42 dBFS）的中间，接缝 8 ms 交叉淡化，逐字时间跟着挪。
"""
import argparse, glob, json, os, re
import numpy as np, soundfile as sf

ap = argparse.ArgumentParser()
ap.add_argument('src'); ap.add_argument('dst')
ap.add_argument('--tighten', type=float, default=0)
ap.add_argument('--only', default='')
a = ap.parse_args()
os.makedirs(a.dst, exist_ok=True)
only = set(filter(None, a.only.split(',')))
wj = os.path.join(a.dst, 'words.json')
out = json.load(open(wj, encoding='utf-8')) if os.path.exists(wj) else {}
TH = -42.0
for f in sorted(glob.glob(os.path.join(a.src, 'L*.json'))):
    k = os.path.basename(f)[:-5]
    if only and k not in only: continue
    d = json.load(open(f, encoding='utf-8')); ws = d['wordList']
    x, sr = sf.read(os.path.join(a.src, k + '.wav')); mono = x if x.ndim == 1 else x.mean(1)
    cuts = []
    if a.tighten > 0:
        hop = int(.01 * sr)
        db = lambda p, q: 20 * np.log10(np.sqrt(np.mean(mono[p:q] ** 2)) + 1e-9)
        for i in range(len(ws) - 1):
            e, s = ws[i].get('e', ws[i]['s']), ws[i + 1]['s']
            if s - e <= a.tighten: continue
            p0, p1 = int(e * sr), int(s * sr)
            quiet = [db(j, j + hop) < TH for j in range(p0, p1 - hop, hop)]
            best, run, st = (0, 0), 0, 0
            for j, q in enumerate(quiet):
                if q: run += 1; st = st if run > 1 else j
                else: run = 0
                if run > best[1]: best = (st, run)
            L = best[1] * hop / sr
            if L <= a.tighten: continue
            rm = L - a.tighten
            cuts.append((p0 + best[0] * hop + int((L - rm) / 2 * sr), int(rm * sr)))
    y = mono.copy(); off = 0; fade = int(.008 * sr); shifts = []
    for c0, n in cuts:
        c = c0 - off; A, B = y[:c], y[c + n:]
        if len(A) > fade and len(B) > fade:
            w = np.linspace(1, 0, fade); y = np.concatenate([A[:-fade], A[-fade:] * w + B[:fade] * (1 - w), B[fade:]]); n += fade
        else: y = np.concatenate([A, B])
        shifts.append((c0 / sr, n / sr)); off += n
    sf.write(os.path.join(a.dst, k + '.wav'), y.astype(np.float32), sr)
    sh = lambda t: t - sum(n for c, n in shifts if c < t)
    units = []
    for i, w in enumerate(ws):
        s0 = sh(w['s']); e0 = sh(ws[i + 1]['s']) if i + 1 < len(ws) else len(y) / sr
        units.append([re.sub(r'[\s，。：、？！；,.:!?]', '', w['w']), round(s0, 3), round(min(e0, sh(w.get('e', w['s'])) + .12), 3)])
    out[k] = {'dur': round(len(y) / sr, 3), 'u': units}
    print(k, round(d['duration'], 2), '->', out[k]['dur'], f'（剪 {len(cuts)} 处）' if cuts else '')
json.dump(out, open(wj, 'w', encoding='utf-8'), ensure_ascii=False)
