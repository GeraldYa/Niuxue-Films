# 04 活体实机录屏（`living-screencast`）做片笔记

> 整支片就是一次 Claude Code 会话的「录屏」：光标是你，像素小家伙 Clawd 是 AI。「用什么」落在启动横幅和路径上，「怎么说」是一句话打进输入框、再被反问一轮，「适合拍什么」交给它做出来的番茄钟演示片，由里面的像素番茄演。

| 项 | 数 |
|---|---|
| 成片 | 83.1 s（`DUR` = 83.098），1080×1440，30 fps，17,402,715 字节（≈16.6 MiB），−16.0 LUFS（LRA 4.1 LU） |
| 渲染 | 2493 帧，`video.mjs --workers 4` 用 23 s（改片尾后重渲用 21 s）；`mix.py` 全合成，跑一遍约 47 s |
| 配音 | 13 句，对齐全 100%；原始 67.0 s，压停顿后 62.7 s |
| 状态 | 存着没发（我 09-28：「不发，先存着」）。成片盘 `2026-09-27 风格片04 一句话让AI做出录屏动画.mp4` |

下文只写文件名的（`film.js`、`main.js`、`ui.js`、`clawd.js`、`poster.js`、`mix.py`、`index.html`）都在 `films/04-living-screencast/` 下；`core/`、`styles/`、`tools/` 开头的是仓库根下的路径。

---

## 1. 构思

风格的招牌母题（`styles/living-screencast/STYLE.md` §1–§3）：界面全部重画、推多近字都锐利；两个演员，光标 = 用户，小家伙 = 软件；小家伙只站在界面元素的上沿；每个动作都引起一次界面变化；录屏软件的镜头（跟随、推近、甩镜）。三样干货逐条对到母题上：

| 干货 | 画面 |
|---|---|
| 用什么：AI 编程助手 | 启动横幅（`banner`）里的「Claude Code」，Clawd 跳上去，字被高亮 |
| 用什么：免费开源库 | 当前路径 `~/lemo-opuscar`：Clawd 跳过去，光标点一下。库名只在画面上，旁白说「名字就在路径里」 |
| 怎么说：一句话 | 那句话随念白一个字一个字打进输入框，Clawd 踩着输入框上沿跟光标走 |
| 怎么说：先问一轮 | 助手回「开工前，先问你三件事」，三问一个个弹出，Clawd 头顶问号 |
| 门道 | 镜头推到 5.2 倍，对准代码里的「25:00」，加聚光暗角，字照样锐利 |
| 光标是你、小家伙是 AI | 光标摸 Clawd 的头（冒心）；Clawd 挥手；读文件时在那一行上冲刺，写代码时掏出像素铅笔 |
| 适合拍什么 | 播放窗里放它做好的番茄钟演示片：像素番茄踩「开始」（软件教程），跳上「白噪音 NEW」（新功能上线），提示气泡「点这里，开始专注」弹出、番茄跳到「重置」（新手引导） |

- **结构**：四章就是工作流四步（01 说一句话 / 02 先问一轮 / 03 自己开工 / 04 出片），章节签用 STYLE §2 的信息层。
- **开头**：前 2.2 s 没有旁白，只有终端里敲 `claude`、logo 冒出来。第一句「这不是录屏。」跟观众眼睛看到的正好反着来，接着推到 3.1 倍当证据，然后 logo 化身成 Clawd：「连这个小家伙也是。」
- **口吻**：短句，第二人称，用风格自己的词（录屏、光标、小家伙），转折句是「门道在这儿」。
- **结尾**：逐词跳字的片尾卡（STYLE §3.9），Clawd 踩着「先收藏 / 下一期 / 换一种风格」跳，最后一脚落在「换一种风格」上，大和弦。
- **没走的路**：第一次读风格时想过把 Clawd 换成自画的像素场记板小人；正式开工时改回 Clawd，场景定为 Claude Code 命令行。记录里没写改回来的原因。
- **假项目**：`~/tomato-timer` 番茄钟 App 是演示用的，里面的文件名、行数、62 秒成片都是示意（README 有写）。

## 2. 分镜

时刻用 `film.js` 的 `build()` 按 `voices/words.json` 算出来，单位秒。

| 时间 | 画面 | 台词（要点） | 手法 |
|---|---|---|---|
| 0–2.2 | 竖长终端敲 `claude` 回车（1.30），logo 分几拍冒出（1.50 / 1.65 / 1.80 各一声方波「哔」），右边三行信息淡入 | — | 开头 0.5 s 从米白淡入；镜头 1.7→1.75 倍，贴终端左沿 |
| 2.2–3.8 | logo 眨一下眼（2.97） | L01 这不是录屏 | 眨眼挂在「录」上 |
| 4.15–8.31 | 4.35 起用 1.6 s 推到横幅 3.1 倍，7.57 拉回 2.0 倍 | L02 每个字、每个按钮都是重新画的 | 推近证明字锐利 |
| 8.61–11.30 | logo 抖（9.08 起）；化身（9.68–10.23），象限像素飞成方像素；Clawd 落在 logo 原位（10.45，冒「!」），大跳到输入框上沿（11.30，火花） | L03 连这个小家伙也是 | logo 化身（匹配剪辑）；落地时乐队进 |
| 11.85–12.7 | 像素块转场：「39 种风格 · 第 4 种 / 活体实机录屏」 | — | 片名转场兼 01 章转场；盖满时用 0.1 s 换机位 |
| 12.9–18.71 | Clawd 慢跳上「Claude Code」（这一跳 12.35–14.44）并高亮；跳到路径（16.32）；光标点路径（17.76） | L04 助手 + 开源库，名字在路径里 | 高亮挂「编程助手」「开源库」 |
| 19.06–27.69 | 光标点输入框（19.92），Clawd 跳到光标旁（21.03）；那句话随念白打出（21.03–25.84），再补「，代码在 ~/tomato-timer」；回车发送（27.69），HUD 显示「↵ 发送」 | L05 跟它说一句话 | 打字摊进念白；Clawd 踩移动地面；镜头跟光标 |
| 28.44 | 转场「02 先问一轮」 | — | |
| 29.39–37.51 | 回复行打出（29.39）；三问弹出（32.78 / 34.18 / 34.94），Clawd 头顶问号、眼睛看左；用户打「都没有，你来做，直接出片」，回车（37.51，Clawd 举手、冒绿勾） | L06 开工前先问你一轮 | 问号道具；「↵ 回答」 |
| 38.11 | 转场「03 自己开工」 | — | |
| 39.16–44.69 | 右上角「▶▶ 4×」；Read AGENTS.md / STYLE.md / App.tsx，Clawd 逐行跳，那行高亮并标上「读过」；Write TREATMENT.md 掏铅笔走；Write ui.js 冒出三行代码（42.99 / 43.39 / 43.73） | L07 读说明、写分镜、一屏一屏重画 | 快进标签 + 十六分沙锤 |
| 45.04–52.33 | 1.8 倍看代码；49.21 起用 1.3 s 推到「25:00」5.2 倍，加聚光暗角；52.33 甩回 1.5 倍 | L08 门道在这儿 | 聚光冻结；抽鼓；甩镜模糊 |
| 52.38–61.08 | 光标摸头（53.07，冒心）；挥手（54.41）；Read Timer.tsx 那行上冲刺（56.46–57.72）；Write film.js 掏铅笔（59.20–61.08） | L09 光标是你，小家伙是 AI | 两个演员互动 |
| 61.18–65.53 | Bash build.sh + 进度条 + `Rendering…`；转场「04 出片」（61.58）；进度条跑满 1860/1860 帧（63.87）；「片子好了…（62 秒）」（64.15） | L10 等它忙完，片子就出来了 | 进度嘀嗒声 |
| 65.58–67.43 | Clawd 一脚踩在「片子好了」那行（65.58，六颗火花）；Bash open（65.83）；QuickTime 窗弹出（66.13）；Clawd 跳上窗顶 | — | 因果：一踩就开片 |
| 66.53–71.79 | 片中片：番茄踩「开始」（68.16，倒计时开始走）；「白噪音 NEW」弹出（69.05），番茄跳上去；提示「点这里，开始专注」弹出（70.57），番茄跳到「重置」；片中角标依次是 01 软件教程 / 02 新功能上线 / 03 新手引导 | L11 最适合拍… | 三个用途各演一下 |
| 72.14–75.72 | Clawd 说到「交给」（74.44）时挥手 | L12 交给水墨和皮影 | |
| 75.97–83.10 | 终端和播放窗缩小淡出，出片尾卡；Clawd 跳上「活体实机录屏」，再逐词跳（76.77 / 77.98 / 78.86，最后一跳是大落地 + 八颗火花）；80.30 出出处小字；82.40 起淡出 | L13 先收藏…（不上字幕，画面上已有大字） | 逐词跳字 |

## 3. 关键手法

来源：`clawd.js` 跟 demo 一模一样，只在末尾加了 `QMARK`、`tomato`。
- `ui.js`、`index.html` 按 demo「状态 → HTML 字符串」的写法重写成竖版。
- `film.js` 的 `Actor`、`Cursor`、`typing`、镜头骨架来自 demo；中文挂字、排时刻、函数镜头目标、全部分镜是新写的。
- `main.js` 新加了世界坐标锚点、终端滚动、`tomatoAt()`、封面模式，去掉了 demo 的明暗双层。
- `mix.py` 用 demo 的 `sound.py` 骨架，采样全部换成合成。

### 3.1 时刻全是推出来的；打字跟着念白走
- **效果**：画面的事（化身、打字、发送、转场）要占时间，旁白得等；那句话要跟着念出来的字一起打。
- **做法**：`VO` 不写死。下一句从上一句结束 + 间隙开始，中间有画面的事就从那件事结束算。
  - `typing()` 加了 `span` 参数，把整句摊进 `[t0, t0+span]`：从 `at('L05','用')` 打到 `at('L05','示',0,'e')`。
  - 字符用 `[...text]` 拆，中文逗号后多停 0.1 s。代码在 `films/04-living-screencast/film.js`。
- **好处**：重配一句，后面整条自动顺延，配乐跟着 `events.json` 走，按 events → mix → video 重跑就行。这跟 SHORTS.md §3 的「后面一格不动」是两种做法，看引擎选。
```js
function typing(t0, text, cps = 12, seed = 1, kind = 'key', span = 0) {
  const T = []; let t = t0; const chars = [...text];
  const step = i => { const r = hash(seed * 31 + i * 7.3); return (1 / cps) * (.55 + r * .9) + (chars[i] === ' ' ? .03 : 0) + ('，,'.includes(chars[i - 1] || '') ? .1 : 0); };
  let tot = 0; for (let i = 0; i < chars.length; i++) tot += step(i);
  const k = span ? span / tot : 1;
  for (let i = 0; i < chars.length; i++) { t += step(i) * k; T.push(t); ev(t, kind, { v: .6 + hash(seed * 31 + i * 7.3) * .4, sp: chars[i] === ' ' ? 1 : 0 }); }
  return T;
}
// build()：T.type0 = at('L05', '用') - .05; T.type1 = at('L05', '示', 0, 'e');
//          TY.sent = typing(T.type0, SENT, 12, 5, 'key', T.type1 - T.type0);
```
- `at()` 先把一句的逐字单元拼成字符串再找，所以被拆成字母的英文（`A`/`I`、`A`/`p`/`p`）也能按「AI」「App」挂。

### 3.2 镜头跟着 DOM 元素走
- **效果**：像录屏软件那样自动跟随：跟着光标、跟着新冒出来的那一行，推到「25:00」这个词上。
- **做法**：`cam()` 的目标可以是 `[cx,cy,z]`，也可以是函数 `A => [cx,cy,z]`，每帧用当帧量到的锚点重算，返回 null 就跳过这一步。
  - 各步按顺序叠，缩放在对数空间插；最后 `fit()`：缩放不小于 1、中心夹在画内，永远拍不到屏幕外面。再加一点微漂。
- **注意**：走完的步骤也每帧重算目标，所以终端往上顶时镜头一直锁着那一行。反过来，挂在还没出现的元素上的那一步，会推迟到元素出现那一帧一下子到位（见 §7 遗留）。
```js
const Lx = z => 40 + 524 / z;                                  // 让终端左沿留在画面里的镜头中心 x
const fit = ([x, y, z]) => { z = Math.max(1, z); const hw = 540 / z, hh = 720 / z; return [clamp(x, hw, 1080 - hw), clamp(y, hh, 1440 - hh), z]; };
export function camAt(t, A) {
  let v = CAM0.slice(); v[2] = Math.log(v[2]);
  for (const m of MOVES) { if (t <= m.t0) break; const p = EASE[m.e]((t - m.t0) / m.d);
    let to = typeof m.to === 'function' ? (A ? m.to(A, t) : null) : m.to; if (!to) continue; to = fit(to);
    v = [lerp(v[0], to[0], p), lerp(v[1], to[1], p), lerp(v[2], Math.log(to[2]), p)]; }
  return fit([v[0] + Math.sin(t * .7) * 1.0, v[1] + Math.sin(t * .53 + 1) * .8, Math.exp(v[2])]);
}
cam(T.spot, 1.3, A => { const p = A('k2500', .5, .5); return p ? [p.x, p.y - 6, 5.2] : null; }, 'eio');   // 推到「25:00」
```
- **打字时跟光标**：`cam(T.type0 + .2, T.type1 - T.type0, A => { … [Math.max(Lx(1.7), c.x - 120), 395, 1.7] }, 'lin')`。目标一直在动，进度线性走，越到后面贴得越紧。
- **转场下换机位**：`cam(T.wipe0 + .45, .1, …)`。像素块盖满时用 0.1 s 挪好（demo 的招）。

### 3.3 锚点按世界坐标缓存
- **问题**：镜头要靠锚点算，锚点又得在带着镜头变换的层里量，两边互相依赖。
- **做法**：先设单位镜头；锚点第一次被问到才量，按「量那一刻生效的镜头」`cur` 换算成世界坐标，存进本帧缓存；算出真镜头后改 `cur`，再应用。后面精灵层才问到的新锚点，会按真镜头反算，也对得上。坑的来龙去脉见 SHORTS.md §6。代码在 `films/04-living-screencast/main.js` 的 `render()`。
```js
let cur = [540, 720, 1]; for (const el of [wL, spr]) el.style.transform = tf(cur);
const cache = {};
const A = (key, fx = .5, fy = 0) => {
  let w = cache[key];
  if (w === undefined) { const el = wL.querySelector(`[data-a="${key}"]`);
    if (!el) w = null; else { const r = el.getBoundingClientRect(), [kx, ky, kz] = cur; w = { x: (r.left - 540) / kz + kx, y: (r.top - 720) / kz + ky, w: r.width / kz, h: r.height / kz }; }
    cache[key] = w; }
  return w && { x: w.x + w.w * fx, y: w.y + w.h * fy, w: w.w, h: w.h }; };
const cam = FM.camAt(t, A), [cx, cy, z] = cam;
cur = cam; for (const el of [wL, spr]) el.style.transform = tf(cam);
```

### 3.4 速度推出来的动态模糊
- **效果**：只有甩镜才拖影，慢推一直清楚（STYLE §3.6）。
- **做法**：用同一份锚点再算上一帧（`t - 1/30`）的镜头，差值乘缩放，就是屏幕上每帧挪了多少像素。超过 26 px/帧才模糊：模糊半径 =（速度 − 26）× 0.3，封顶 30。
  - 模糊加在没做变换的外壳 `#mbw` 上（`<filter id="mb"><feGaussianBlur id="mbg">`），方向是屏幕方向。
  - 两次都用本帧的 DOM，新行把内容顶上去不会带出假速度。推近用 `eio` 慢推 1.3 s，回拉用 `whip`（五次方缓动）0.45 s 甩回去。
```js
const [px, py] = FM.camAt(t - 1 / 30, A), vx = (cx - px) * z, vy = (cy - py) * z;
const bx = Math.min(30, Math.max(0, Math.abs(vx) - 26) * .3), by = Math.min(30, Math.max(0, Math.abs(vy) - 26) * .3);
mbg.setAttribute('stdDeviation', `${bx.toFixed(2)} ${by.toFixed(2)}`); mbw.style.filter = bx > .6 || by > .6 ? 'url(#mb)' : '';
window.DBG = { bx, by, vx, vy, cam, prev: [px, py] };        // 调试口，见 §8
```

### 3.5 终端整行上顶
- `frame(t)` 每帧从头把所有行重新列一遍（纯状态，不存历史）。`ui.js` 把行和输入框一起放进 `.body > .scroll`，`.body` 超出部分藏起来。
- `main.js` 渲完 HTML 立刻量高度，超出多少就往上顶多少，下面留 26 px：`` const over = sc.offsetHeight + 26 - bd.clientHeight; if (over > 0) sc.style.transform = `translateY(${-over}px)`; ``
- 输入框在滚动内容里，内容一满就贴在窗底，跟真终端一样。锚点在顶完之后才量，小家伙和镜头自动跟着上移。新行滑入用的是 `transform`，不改 `offsetHeight`，滚动当帧就到位。

### 3.6 Clawd 的站位：挂在字上，踩移动的地面
- **锚点挂行内 span**：`ui.js` 的 `line()` 把 `data-a` 放在行内文字的 `<span>` 上（回复、问题、工具、代码、用户消息），进度条挂在 `.bar` 上，要推近的词单独包一层（`<span data-a="k2500">25:00</span>`）。
- **打字行不抖**：回复行逐字打出，没打的部分用 `opacity:0` 先占着位，span 宽度不变，站在 80% 处的 Clawd 不会跟着字滑。
```js
case 'a': { const w = [...m.text], n = Math.round(w.length * Math.min(1, m.p ?? 1));
  return `<div class="tl" style="${s}"><span class="bul">⏺</span><span${id}>${esc(w.slice(0, n).join(''))}<span style="opacity:0">${esc(w.slice(n).join(''))}</span></span></div>`; }
```
- **移动的地面**：打字的时候，x 取光标、y 取输入框上沿那条线：`.stand(T.type0, T.send, A => { const r = A('rule', 0, 0), c = A('caret', .5, 0); return r && c ? { x: c.x + 34, y: r.y } : null; }, { eyes: 'd' })`。发送后站到用户消息 50% 处（`still: true`，不跟拍呼吸）。
- **`at_(key, fx, fy, dx, dy)`**：元素暂时不在时沿用上一次的位置（逐帧顺序渲才成立）；元素还没出现过就返回 null，这一段 Clawd 不画。

### 3.7 Clawd 的动作
都是 `Actor` 的分段（`stand` / `walk` / `jump` / `hide`），再由 `main.js` 的 `sprites()` 按段标记画道具。
- **跳**（demo 原样）：二次贝塞尔弧线；起跳前 0.14 s 蓄力压扁，落地 0.22 s 阻尼回弹加尘土。站着时每拍（`t % B`，B = 0.6 s）轻压一下，跟配乐拍点同一个网格。
- **读文件**：三次短跳，逐行落在 `t-agents` / `t-style` / `t-app` 上（fx 0.30 / 0.35 / 0.40）。每次落地响一声方波（C6 / E6 / G6）、冒绿勾，那行高亮 0.45 s 并标上「读过」，再出 `⎿ Read N lines`。
- **跑、掏铅笔、顶问号**：
```js
 .jump(T.r2 + .1, T.run0, at_('code-0', .62, 0), at_('t-read2', .06, 0), 50)
 .walk(T.run0, T.run1, at_('t-read2', .06, 0), at_('t-read2', .8, 0), { dash: true, eyes: 'd' })    // 跑到「跑」字念完
 // …
 .walk(T.pen0, T.pen1, at_('t-write2', .1, 0), at_('t-write2', .72, 0), { pencil: true, ease: x => x, eyes: 'd' })   // 匀速 = 在写
// main.js sprites()：道具跟着脚底 / 头顶（top = c.y - c.px * 10）
if (s && s.pencil) h += CW.PENCIL(c.flip ? c.x - 9 * c.px - 6 * c.px : c.x + 6 * c.px, c.y - 7 * c.px, c.px);
if (s && s.dash) h += CW.speedlines(c.x, c.y, 1, seg(t, s.t0, s.t1) * .8 + .1, 4);
if (t > T.q[0] - .2 && t < FM.VO.L06 + words.L06.dur + .1) h += CW.QMARK(c.x + 34, top - 60, 5, Math.min(seg(t, T.q[0] - .2, T.q[0]), 1));
```
  - 道具和小家伙在同一张像素网格上（`pixart(rows, {px})`，px 跟 Clawd 一样）。`QMARK` 是新做的 5×10 道具，第一问前 0.2 s 淡入，L06 念完才收。
- **踩下**：两段跳，先从进度条跳到「片子好了」上方 30 px，再用 0.3 s 砸下去（`{ big: true }`）：大落地音 + `stomp` + 镲 + 底鼓，一圈六颗火花。0.25 s 后出 `Bash(open …mp4)`，再过 0.3 s 弹出播放窗（缩放 0.2→1，`back` 缓动）。
- **摸头**：光标的目标直接用 Clawd 在那一刻的头顶。点下去 Clawd 压扁 0.3 s、闭眼 0.5 s、冒一颗心，响 `boing`（420 Hz、14 Hz 颤音）。
  `.move(T.pet - .5, T.pet - .03, A => { const c = C.eval(T.pet - .05, A); return c && { x: c.x + 4, y: c.y - c.px * 10 - 2 }; }, 20).click(T.pet)`
- **片中片的番茄**（`main.js` 的 `tomatoAt()`）：12×11 像素番茄，px 4。落点量播放窗里的 `m-start` / `m-new` / `m-reset`，起点站在 App 卡片上沿（`m-app` 22% 处）；跳法和落地回弹跟 Clawd 同一套公式。
- **化身**（demo 的 §3.1 原招，改了几何）：logo 就是 Clawd 那张 18×10 网格，两行并一行画成终端象限字符，眼睛留空。化身 0.55 s，每个像素从象限块（`LOGO.qw × LOGO.qh/2`）插值到方像素，起步随机错开、中途往外甩；眼睛过 60% 变深色，logo 原位留虚线框。代码在 `film.js` 的 `frame()`。

## 4. 声音

- **配音**：我的声音，VoxCPM2 讲解口吻音色，13 句一句一场（导入和 `--tighten` 见 SHORTS.md §3）。压之前最长的停顿：L12「拍情绪？」后 1.20 s，L08「门道在这儿：」后 1.12 s，L09「光标是你，」后 0.96 s。一共剪了 17 刀（L09 一句就 5 刀），67.0 s → 62.7 s。
- **配乐**（`mix.py`，全读 `events.json`，BPM 100）：
  - 高清层：拨弦贝斯、卡林巴、八音盒（`core/audio/pluck.py`）加现做的鼓：底鼓 `kick()` 是 45 + 80·e^(−t/0.035) Hz 正弦扫频，拍手 `clap()` 是间隔 11 ms 的三下 900–5200 Hz 噪声，踩镲、沙锤、嗵鼓（`hat()` / `shaker()` / `tom()`）是滤波噪声和扫频正弦。
  - 像素层：`pulse()` 用谐波叠加出带限方波（到 16 kHz 为止），`crush()` 降位深。两层合起来过一道小房间混响（`S.room`，size 0.33、mix 0.12）。
  - 前奏：2.1 s 起八音盒 Fmaj7 八分琶音，7–10 s 渐强；落地前一小节加拨弦贝斯四拍和上行噪声。
  - 落地后乐队进：Fmaj7 → Am7 → Dm7 → B♭maj7，每小节一个，循环；底鼓一、三拍（三拍后补一个八分），拍手二、四拍，踩镲八分。
  - 高点：每个转场前一拍四个递降嗵鼓（190 → 105 Hz），转场点一声镲；L07 快进加十六分沙锤；推近「25:00」那几秒抽掉底鼓、拍手和反拍卡林巴；踩下是镲 + 底鼓。
  - 收尾：鼓停，F、B♭ 两个长和弦；最后一脚 F1 + 卡林巴 Fmaj9（F3 C4 A4 E5 G5 C6）+ 八音盒十六分上行 + 镲。
  - 方波主题（C6 A5 F5 G5 A5 C6 D6）在落地和最后一脚后各奏一遍；化身时一串方波琶音；片尾三个词各一个音（C5 / E5 / G5）。
  - 拍点网格从 0 起每 0.6 s 一拍，乐队从离落地最近的那拍进：落地 11.30 s，第一拍 11.40 s。demo 是把落地直接定在拍上（8.4 s = 第 14 拍）。
- **拟音**（都从 `ev()` 来）：
  - 键盘是 170 Hz「咚」+ 带通噪声「嗒」，力度有抖动，回车更重；另有光标点击、弹出、发送、工具行两声嘀嗒、进度嘀嗒。
  - 读文件是方波音；写代码是 11 Hz 调幅噪声，像铅笔沙沙声。跳是方波上滑，落地是 110 Hz 方波 + 降位深噪声，步子是降位深短噪声。
  - 甩镜、转场是带通噪声呼啸，化身是 26 个随机方波点；片中片番茄踩按钮是 G3 下滑 + 点击，NEW 和提示弹出各一声「啵」。
- **电平**：人声压缩 + 70 Hz 高通，RMS 定到 −18 dB；音乐 −29 dB（3 s 到结尾前 3 s 这段算）；拟音 −30 dB。人声包络（120 ms 平滑）把音乐压到 0.4，约 −8 dB。最后 1.4 s 淡出，限幅 0.95。各段 RMS：冷开场 −19.4、01 −18.2、03 −18.4、出片 −18.5、片尾 −22.0 dB；mux 后 −16.0 LUFS。

## 5. 竖版改造

SHORTS.md §2 已写「界面重排成竖的」「`Lx(z)` 算镜头中心」，这里补具体尺寸。
- **场景**：demo 是 1920×1080 桌面 + Claude 应用大窗（1700×950），冷开场才有个 760×320 小终端。04 整片就是一扇竖长终端 `TERM = {x:40, y:92, w:1000, h:1310}`，最后弹一个横的播放窗 `QT = {x:90, y:330, w:900, h:540}`（片中片 900×506）。
- **字**：Menlo 21 px、行高 33（`CW = 21*.602`），中文回退 PingFang SC；标题、片尾用 paper-lantern 素材包的 NotoSerifSC（SHORTS.md §4）。demo 用 JetBrains Mono 19 px、行高 30，外加 Inter / Newsreader；demo 自己的 `fonts/` 里只有许可文件，字体文件在它的素材包里。
- **`LOGO` 是算出来的**：从 TERM、内边距 26/20、标题栏 38、`CW`、`LH` 推，化身靠它。改 CSS 要同步改这几个常量。
- **镜头**：画面中心 540/720（`tf()`、`fit()` 的 hw/hh）；终端段的 x 全用 `Lx(z) = 40 + 524/z`，左边留 16 px 屏幕边；播放窗那段中心 x 固定 540，缩放 1.12–1.18。
- **HUD**：章节签左上 (40, 52)，「▶▶ 4×」右上，按键 HUD 左下 bottom 230，字幕药丸 bottom 64、38 px，`{}` 里的字标成陶土色。
- **转场**：18×24 格 60 px 像素块，正好铺满 1080×1440；奶油色小 Clawd 在 y = 930 横穿过去。
- **别的**：壁纸 2280×2640、菜单栏 2280 宽，四边各多出 600 px；片尾卡放在世界层（`desk.end`），镜头能推，Clawd 能站在字上；demo 的明暗双层去掉了。

## 6. 封面

- `?poster=1`：`main.js` 动态加载 `poster.js`，再把 `window.render` 换成空函数，免得 `still.mjs` 调 render 时把封面盖掉。命令：`node core/render/still.mjs films/04-living-screencast 0 --q poster=1`，出来的 `t_0.jpg` 拷成 `cover.jpg`。
- 构图：
  - 上半是片名大字：「一句话」236 px（NotoSerifSC 800）、「让 AI 做出录屏动画」84 px 陶土色、「39 种风格 · 04 活体实机录屏」。
  - 下半是缩到 0.93 的终端，一屏交代完整个流程：命令、虚线 logo 框、那句话、三问、回答、Read / Write、进度条满、「片子好了」。
  - 右下叠一个缩到 0.76 的播放窗，片中片停在 0:03（24:57），带 01 软件教程角标，番茄站在里面。
- Clawd 站在「一句话」上沿 83% 处，位置用 `getBoundingClientRect()` 量大字得到，照「只站在界面上沿」的规矩；px 9，举手笑眼，配三颗火花。
- 复用界面：直接拿 `UI.desk()` 的输出，用正则去掉前面的壁纸和菜单栏，塞进带缩放的外壳：`UI.desk({ term }, 0).replace(/^.*?<div class="term"/s, '<div class="term"')`。

## 7. 返工记录

1. **配音拖**：人声合计 67 s。看逐字时间，是句中停顿长，不是语速慢，压到 0.45 s 后是 62.7 s。这套手工脚本后来做成了 `tools/vo_import.py --tighten`，重导结果跟手工版一模一样。
2. **片名转场盖住落地**：第一次导事件，转场在 11.13 s，Clawd 落到输入框在 11.45 s（乐队也在这里进）。
   - 改法：`T.wipe0` 从化身往后推，`T.morph0 + .77 + .35 + .5 + .55`，即落地后 0.55 s；句间空隙顺手收紧（.45→.35、.9→.6 等），总长 83.58 → 83.10 s。
   - 教训：高点不能被转场盖住，转场时刻要从动作链往后推。
3. **27 张检查静帧**（`still.mjs` 按时刻出图，PIL 拼联系表）：
   - **03 章起整屏糊**：用 `window.DBG` + 调试脚本（§8）一查，40.66 / 43.66 / 50.54 / 52.98 / 56.58 s 的 by 都封顶 30。原因是锚点在换了镜头之后又被量了一次。改成世界坐标缓存（§3.3）后五处全为 0。
   - **终端左沿被切**：所有镜头 x 改用 `Lx(z)`。
   - **小家伙站在行尾空白上**：`data-a` 从整行 div 挪到行内 span。
   - **推近对不准**：原来推的是整行代码的 42% 处，改成专门包出来的 `k2500`，聚光也对它。
   - **片中片**：番茄起点从写死的 `QT.x + 110` 改成站在 App 卡片上沿；提示气泡挪到按钮下面，箭头朝上。
   - **「logo 眼睛没镂空」是误报**：网格和渲染都没问题，那张 3.00 s 的静帧正好赶上眨眼（`T.blink` = 2.97 s，眨 0.16 s）。教训：抽帧先对一眼时间表。
4. **第二轮静帧**：用户消息的锚点也挂到 span 上；发送后 Clawd 从消息 90% 处挪到 50%，别贴右沿。
5. **界面上的字**（边渲第一版边核）：横幅上的「Opus 5.5 · Claude Max」删掉套餐名，因为不知道看的人用哪种；进度条 2250 帧改成 1860（62 s × 30 fps）。
6. **看第一版成片**：每 1.5 s 抽一帧拼表，另抽 50.9 s、69.9 s 两张全尺寸帧。播放窗左沿被切 7 px，片中片镜头 `[540, 610, 1.22]` 改成 `[540, 606, 1.18]`。
7. **片尾出处**：第一版写的是「风格与引擎：开源库 lemo-opuscar（MIT）」。写 SHORTS.md 时对照 01–03，发现缺 CC BY 和 LemoLab × Claude Opus 5.5，改成系列统一写法，重渲 21 s。
8. **遗留**（没返工。写笔记时读代码推出来，09-29 用静帧和 `window.DBG` 逐帧核实过）：
   - 03 章 `t-app`（「明」字结束 + 0.15 = 41.43 s）比 `t-treat`（「写分镜」开始 = 41.32 s）晚。静帧里 41.4 s 先冒出 TREATMENT 那行，41.5 s App.tsx 那行才插到它上面，真终端不会这样。Clawd 41.767 s 还在 App.tsx 行，41.8 s 就闪到 TREATMENT 行（去那行的一跳被前一段盖掉了）。4× 快进下一闪而过。
     - 修法：`t-app` 不晚于 `t-treat`，比如两个都从同一个字链出来再各加偏移。
     - 教训：挂字加固定偏移算出来的时刻，排完要查一遍先后。
   - 02 章「转场下换机位」挂在回复行 `a1` 上，可 `a1` 29.39 s 才出现，比那一步晚约 0.5 s，转场早就结束了。逐帧看：29.367 s 镜头还是 `[402, 497, 1.4]`，29.4 s 一帧跳到 `[390, 480, 1.5]`，推近 7%，没有模糊（两次都用本帧锚点，量不出速度）。29.367 s 前约 0.45 s Clawd 也没画。
     - 修法：这一步的目标先用固定坐标，或者等 `a1` 出现后再用 0.3 s 以上推过去。
   - 12.35–14.44 s 从输入框跳上「Claude Code」那一跳：起跳在片名转场底下（`T.wipe0 + .5`），一直飘到「编程助手」（`T.hlName`）才落，转场散开后还在空中飘约 1.7 s，比别的跳（0.2–1.2 s）慢得多，看着像浮着。
     - 修法：落点时刻不动，起跳挪到转场散开之后。
   - 字幕药丸底边离画面底 64 px，最长一行 25 字（L09），比 SHORTS.md §1 的约 96 px、≤15 字都超了。
   - 片尾比 01–03 多了一行配音署名。SHORTS.md §8 说片尾不署做片人的名，这行留不留，发之前问我。

## 8. 下一期能直接拿走的

- **别的 DOM 界面类风格**：`films/04-living-screencast/main.js` 的 `render()` 骨架整段能用：世界坐标锚点缓存、按锚点算镜头、镜头速度推模糊、内容超出就上顶。
- **`film.js`**：`at()`（中文挂字，跨单元匹配）、`typing(…, span)`、`camAt()` + `fit()` + `Lx()`、`Actor` / `Cursor` / `at_()`，还有「下一句 = 上一句结束 + 间隙，画面的事卡住下一句」的排法。
- **`clawd.js` 的 `pixart(rows, {x, y, px, pal})`**：一行字符串一行像素，任何像素道具、吉祥物都能画，`QMARK`、`tomato` 就是例子。
- **`ui.js` 的写法**：纯函数，状态进 HTML 出；锚点挂行内 span；逐字打出的行用透明余字占位；要推近的词单独包 span。
- **`mix.py`**：合成鼓组、`pulse()`、`crush()`、事件到拟音的对照、闪避和三轨定电平，换风格也能用；配乐的点位全用 `first('hit')`、`all_('wipe')` 这类从 `events.json` 取时刻，画面一改音乐自动跟。
- **封面模式**：`?poster=1` + 动态 import + 空 render。
- **不渲视频查镜头**：用 `core/render/page.mjs` 的 `openDemo()` 打开页面，逐个时刻调 `render(t)` 读 `window.DBG`，几秒出结果。脚本放哪都行，import 指到 `core/render/page.mjs`：
```js
import { openDemo, closeServer } from './core/render/page.mjs';
const { browser, page } = await openDemo('films/04-living-screencast');
for (const t of process.argv.slice(2).map(Number)) {
  const d = await page.evaluate(t => { window.render(t); return window.DBG; }, t);
  console.log(t, JSON.stringify({ bx: +d.bx.toFixed(1), by: +d.by.toFixed(1), cam: d.cam.map(v => +v.toFixed(1)), prev: d.prev.map(v => +v.toFixed(1)) }));
}
await browser.close(); closeServer();
```
- **抽检**：渲前用 `still.mjs <期> t1 t2 …` 按分镜时刻出图，拼 7 列联系表；渲后用 `ffmpeg -i final.mp4 -vf "fps=2/3,scale=216:288"`，每 1.5 s 一帧拼表。

## 9. 本机重出

`films/` 不进 git，这期的源码只在我的 Mac 上：`films/04-living-screencast/`。成片在成片盘。以下在仓库根跑：
```
node core/render/events.mjs films/04-living-screencast
.venv/bin/python films/04-living-screencast/mix.py
node core/render/video.mjs films/04-living-screencast --fps 30 --workers 4 --out films/04-living-screencast/out/video.mp4
LUFS=-16 sh core/render/mux.sh films/04-living-screencast/out/video.mp4 films/04-living-screencast/mix.wav films/04-living-screencast/out/final.mp4 30 0
```
- **封面**：`node core/render/still.mjs films/04-living-screencast 0 --q poster=1`（出在 `films/04-living-screencast/stills/t_0.jpg`）。
- **静帧**：`node core/render/still.mjs films/04-living-screencast 12.3 50.9 69.9 --out <目录>`；加 `--q nosubs=1` 不带字幕。
- **重配音**：配音 build 入盘后进了废纸篓，期目录还在。
  1. 在白板工具里对「2026-09-27 风格片04 录屏配音」跑 `wb scenes` + `wb tts`（只重配一句：`wb tts <期> L07`）；
  2. `.venv/bin/python tools/vo_import.py <wb 期的 work/audio 目录> films/04-living-screencast/voices --tighten 0.45`；
  3. 从 events 那步起重跑。时刻全是推出来的，不用手改。
