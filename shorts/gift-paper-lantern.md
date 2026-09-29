# 纸雕灯影（`paper-lantern`）· 礼物片做片笔记

> 私人片，不发号。这里只记做法，给以后的纸雕灯影（系列 07 期）用。
> 片子目录在 `films/` 下，目录名带主角昵称，下文写成 `films/<礼物片>/`；下文不带路径的 `film.js`、`main.js`、`figures.js` 等都在它的 `src/` 里，`render/`、`sheet.html`、`mix.py` 在目录根。
> 代码里人物的变量名、函数名是真人称呼。下面的片段一律换成角色名：`host` 主角、`walker` 提灯的人、`guard` 门口的人。对照源码按行号找。

| 项 | 数 |
|---|---|
| 成片 | 79.6 s（ffprobe 79.63 s）· 1080×1440 · 30 fps · H.264 + AAC · 23.8 MB · −16.0 LUFS（LRA 4.5 LU） |
| 渲染 | 2389 帧 · SSAA 2（内部 2160×2880）· 本片 `render/video.mjs` 4 路 102 s（Apple M1 Pro）；之前两次整片重渲 2419 帧，84–91 s |
| 配音 | 14 句，合计 56.8 s。4.2 s 起第一句，71.05 s 说完，之后 8.6 s 只有画面和配乐 |

## 1. 构思

- **层 = 守护者**：每位守护者一张纸，按旁白一张张加进同一只灯箱。最后满框时所有人都在。
- **光源 = 她的窗**：背光中心 `uLight` 放在窗上（demo 放在月亮上），离窗越近的纸越透、越暖。开场第一个亮的就是这扇窗（STYLE.md §2：亮窗 + 窗里的剪影是这个风格最强的画面）。
- **景深 = 轮到谁**：每拍对焦当事人那层，其余虚掉。
- **桌面 = 礼物**：首尾是桌上的实物灯箱。demo 的茶具月饼换成一部亮着直播间界面的手机。
- **一镜到底**：一个 scene，不切、不叠化，「换镜」就是镜头在层间挪位。人只加不减，结尾全景本身就是结论。
- **每人一个动作**：落下、飞来、滑入带下雨、冒出、走进来、现身弹气泡、连线。别都用淡入。
- **结构**：开灯（0–8 s）→ 一层层加（13–55 s，7 位，一人一句 3.5–5.4 s）→ 高潮（55–66 s，光最亮）→ 收（66–79.65 s：点题、名字条、拉回桌前、素材署名）。

## 2. 分镜

最终版时间，按 `timeline.json` 和 `film.js` 的 `T` 算。

| 时间 (s) | 画面 | 手法 |
|---|---|---|
| 0–2.4 | 暗房间，灯箱没亮，右前方手机屏亮着 | 相机 z 1.55 → 1.5，fov 30；0.6 s 开关声 |
| 1.0–5.0 | 开灯：天幕、月亮，6 层纸由远到近透光，主光、远楼窗格、街灯 | `lamp` 1.0–3.4；各层 `uTrans` 错开 .3 s；主光 2.2–4.4 |
| 2.4–5.6 | 推进灯箱，停在满框 | z 1.5 → .7，fov 30 → 34；4.0 s 前对焦箱口 |
| 6.6 | 楼中间那扇窗亮，窗里是坐着对麦的主角剪影 | 挂第 1 句「亮」；窗纸是暗色，亮全靠发光图 |
| 7.4–8.2 | 推近窗 | z .5 |
| 13.1 | 左侧竖排片名 + 红印浮现 | 第 2 句结束 +.15；`show()` 1.4 s，上浮 6 mm |
| 13.3–14.3 | 拉回满框（第 3 句） | `BOXV` |
| 20.2 | 第 1 位：屋檐和窗框从上面落下，磕一下 | 挂「搭」−.2；knock |
| 22.9–24.8 | 第 2 位：鸟从右上飞来，叼着小箱子落上窗台 | 身体、翅膀两张纸；弧线飞行 |
| 28.5–34.3 | 第 3 位：祥云滑到楼顶；30.7 s 起雨只下在两边 | 云 `eo` 1.4 s；雨 3.6 s |
| 35.2–37.8 | 第 4 位：窗台三个玩偶依次冒出，一颗心升起散掉 | 间隔 .22 s，`back` 过冲 |
| 38.7–43.6 | 第 5 位：提灯的人从左走到亮着的小店窗前 | 镜头推到 z .22；光圈 16 → 4 |
| 44.3–51.9 | 第 6 位：门口的人在亮门前现身；48.7 s 弹气泡，3.2 s 后收 | z .29 |
| 52.4–54.7 | 第 7 位：右上几颗星连成电路走线 | `uClip` 圆形揭开；sparkle |
| 55.6 | 高潮：远处一扇冷光窗亮 | ping |
| 58.0 | 主角蹦两下，弹出气泡 | boing |
| 59.6–66 | 三层纸灯往上升，她的窗越烧越亮，冷光窗暗下去 | 镜头拉到 z .74 |
| 64.0–66.2 | 推近窗（点题上半句） | z .42 |
| 68.05 | 最前一层名字条亮 | 满框 z .72，对焦名字层；配乐最高点 |
| 71.65–75.25 | 拉出灯箱回到桌前，手机还亮着 | z .72 → 1.45，fov 34 → 30 |
| 75.85 | 片尾素材署名淡入（DOM 小字） | 挂 `T.out + 4.2` |
| 78.25–79.65 | 淡黑 | `fade` 最后 1.4 s |

## 3. 关键手法

### 3.1 纸层栈：一次建全，先藏后显（`film.js` 第 38–154 行）

- `add()` 默认满幅 `.358×.478`；小道具给 `w/h/x/y` 和锚点 `ax/ay`（锚点就是网格原点，转、缩都绕它）。
- 所有层在 `build()` 里一次建好，画布只画一次。守护者的层随即 `visible = false`，到拍再显形。
- 开灯前全黑：`S.amb.intensity = 0`。背光中心 `light: [0, -.03, -.07]`（她的窗），`lightR: .13`；顶灯 `keyPos: [0, .25, .01]` 斜打向后下方，层间软影是引擎自带的 VSM。
- 贴得很近或自发光的层一律 `shadow: false, recv: false`：窗里的主角离楼只有 0.8 mm，还有气泡、雨、星座、纸灯、名字条（STYLE.md §8）。
- `update(t)` 只看 t，原值用 `??=` 缓存一次。所以 4 路并行、从任意帧开渲，结果都一样。

| z | 层（远层亮而透，近层暗而实） | `trans` | `glow` |
|---|---|---|---|
| −.138 / −.132 | 天幕渐变 + 240 颗星（`skyPanel`，不受光）/ 月亮 | — | — |
| −.126 / −.118 | 星座连线 / 远处祥云 | .2 / .85 | 2.4 / — |
| −.104 / −.088 | 远楼 / 中楼天际线，窗格随机亮 16% / 12%（`skyline()`） | .6 / .4 | .55 / .7 |
| −.0875 | 远处冷光窗（高潮用） | 0 | 2.2 |
| −.07 / −.0692 | 她那栋楼（窗 + 半亮的楼门）/ 窗里的主角剪影 | .25 / .02 | 2.6 / — |
| −.064 … −.05 | 屋檐、主角的气泡、鸟、玩偶和心、楼顶的云、两条雨 | 0–.9 | 气泡、心 1.8 |
| −.04 / −.032 / −.03 | 街面和亮着的小店 / 提灯的人 / 门口的人 | .2 / .05 | 1.4 / 灯笼 2.4 |
| −.078 / −.048 / −.022 | 三层纸灯（高潮） | .05 | 2.2 |
| −.014 / −.012 | 前景草 / 名字条 | .05 / .3 | — / 1.3 |

### 3.2 一层层加进来：`show()` / `pop()`（`film.js` 第 212–242、255–256 行）

- 纸材质是 `alphaTest .5` + `alphaToCoverage`，不走透明混合，**opacity 淡入不起作用**。
  - `show()` 把 `material.color` 和 `uTrans` 从 0 一起拉到原值：纸从黑里亮出来。
  - `pop()` 用 `back()` 过冲放大 .35 s，收的时候 .4 s 缩掉。气泡用它。
- 其余动作：
  - 屋檐从上方 6 cm 落下，落定后按 `.0015·e^(−12t)·sin(40t)` 抖一下；
  - 鸟翅膀单独一张纸，锚在肩上 `rotation.z = .9·sin(34t)`，飞行路径在 `lerp` 上加 `sin(e·π)·.05` 拱起；
  - 提灯的人 `ss` 横移，加 `|sin(14k)|·1.5 mm` 颠步。

```js
function show(m, t, t0, d) { const k = ss(seg(t, t0, t0 + d)); m.visible = k > 0;
  if (m.visible) { m.material.color.setScalar(k); m.material.userData.u.uTrans.value = (m.userData.tr0 ??= m.material.userData.u.uTrans.value) * k; } }
function pop(m, t, t0, t1 = 1e9) { const k = seg(t, t0, t0 + .35), o = seg(t, t1, t1 + .4); m.visible = k > 0 && o < 1;
  if (m.visible) { const s = Math.max(.001, back(k, 2) * (1 - o)); m.scale.set(s, s, 1); m.material.userData.u.uGlowLit.value = (1 - o); } }
// 玩偶：锚点在脚，只拉 scale.y，back 过冲 =「冒出来」
dolls.forEach((d, i) => { const k = seg(t, T.dolls + i * .22, T.dolls + i * .22 + .35); d.visible = k > 0; d.scale.set(1, Math.max(.001, back(k, 2.2)), 1); });
```

### 3.3 剪影：关键点样条，按真人比例刻（`figures.js` 第 15、32 行）

- 写法同 `people.js`：身高归一到 1、原点在脚、y 朝上；点的第三个值 1 = 尖角；`spline()` 走 Catmull-Rom。
- 腿单独成形，前后错开就是在走路。`people.js` 的 `arm()` 返回手心坐标，挑灯杆从手心接出去。画发光图那遍全部涂黑，只有灯笼进发光图（`lantern(…, glow ? x : null)`）。
- 尺寸对齐场景：门 .032×.042 m，小店窗 .064×.044 m；门口的人 .037 m 高，提灯的人 .044 m。人显小就把镜头推近，别放大人。
- 定妆页 `sheet.html`：纯 Canvas2D，不起 WebGL，几秒出图。上半两个 560 px 大图看轮廓；下半按片中实际大小（门 273 px，人 250–290 px）配同色亮块，看认不认得出。

```js
const fill = (x, s, pts) => { spline(x, s, pts); x.fill(); };
const mirror = pts => pts.map(p => [-p[0], p[1], p[2]]);
export function guardFig(x, s) {                     // 叉腰、高马尾：身体 + 胳膊 + 镜像胳膊 + 马尾 + 头 + 脖子
  fill(x, s, G_BODY); fill(x, s, G_ARM); fill(x, s, mirror(G_ARM)); fill(x, s, G_TAIL);
  x.beginPath(); x.ellipse(0, .925 * s, .056 * s, .068 * s, 0, 0, TAU); x.fill(); x.fillRect(-.022 * s, .82 * s, .044 * s, .06 * s);
}
// walkerFig(x, s, glow)：后腿、前腿、长外套三块，再接胳膊，从手心画杆挂灯笼
x.save(); x.translate(.012 * s, .775 * s); const [hx, hy] = arm(x, s, -1.0, 1.25, { w: .058 }); x.restore();
```

### 3.4 时刻挂在字上，画面和拟音同一张表（`film.js` 第 157–165 行）

- `at()` 在 `main.js` 第 16–21 行，用法见 SHORTS.md §3。`events` 紧挨着 `T` 写，时长 `d` 用两个时刻相减。
- 改台词、换配音后重跑 `render/timeline.mjs`，画面和拟音一起挪。

```js
const T = {
  lampOn: 1.0, winOn: at('L01', '亮'), titleIn: C.L02.end + .15,
  eave: at('L04', '搭') - .2, /* …每位守护者一两个时刻 */ stars: at('L10', '星') - .2, stars1: at('L10', '线', 0, 'e'),
  /* … */ lan: C.L12.at - .1, lan1: C.L12.end + 1.6, glow: C.L13.at, names: at('L14', '一') - .2, out: C.L14.end + .6,
};
const events = [{ t: .6, type: 'switch' }, { t: T.lampOn, type: 'shimmer' }, { t: T.winOn, type: 'chime' }, /* … */
  { t: T.walker, type: 'steps', d: T.walker1 - T.walker - .3 }, /* … */ { t: T.stars, type: 'sparkle', d: T.stars1 - T.stars },
  /* … */ { t: T.out, type: 'room' }];
// main.js：window.EV = F.events → render/timeline.mjs → timeline.json → mix.py 按 type 合成
```

### 3.5 镜头：桌面 → 灯箱 → 桌面，每拍停住（`film.js` 第 169–192、245 行）

- 首尾四个关键帧在房间里，中间 13 拍。每拍两个关键帧：到位、停住；离下一拍 1 s 起步。
- 满框 `BOXV` 是 z .7、fov 34。按 fov 算，到纸层 .77 m 时竖向视野约 .47 m，正好装下 .478 高的纸。
- `camAt()` 用 `eio` 插值位置、注视点、fov；`aim()` 再叠手持微动（`hand: .0005`）。

```js
const BOXV = [[0, -.01, .7], [0, -.01, -.07]];                                // 满框：位置、注视点
const beats = [[C.L02.at + .2, [0, -.025, .5], [0, -.028, -.07]], [C.L03.at + .4, ...BOXV], /* … 共 13 拍 */];
const K = [[0, [0, .1, 1.55], [0, -.02, -.07], 30], [2.4, [0, .095, 1.5], [0, -.02, -.07], 30], [C.L01.at + 1.4, ...BOXV, 34], [C.L02.at - .6, ...BOXV, 34]];
beats.forEach(([ta, p, q], i) => { const next = i + 1 < beats.length ? beats[i + 1][0] : T.out;
  K.push([ta, p, q, 34], [Math.max(ta + .3, next - (i === beats.length - 1 ? 0 : 1.0)), p, q, 34]); });   // 停住，提前 1 s 走
K.push([T.out + 3.6, [0, .09, 1.45], [0, -.02, -.07], 30], [E.DUR + 1, [0, .092, 1.47], [0, -.02, -.07], 30]);   // 拉回桌前
```

### 3.6 按拍对焦、收光圈、减辉光（`film.js` 第 246、248–251 行）

- 对焦层按拍跳，不插值。跳点（4.0、38.4、51.8、67.65、73.25 s）都落在镜头挪位途中，被运动盖住。
- 提灯的人、门口的人两拍把 `sharp` 拉到 1：`aper` 16 → 4，`bloom.strength` .34 → .22。不这么做，细剪影会被亮门、亮窗洗成半透明的橘色（SHORTS.md §6）。

```js
focusZ = t < T.lampOn + 3 ? .0 : t > T.out + 1.6 ? .0                 // 房间里：对焦箱口
  : (t > T.walker - .3 && t < T.stars - .6) ? -.032                    // 街上两拍：人物层
  : (t > T.names - .4 && t < T.out) ? -.04 : -.066;                    // 名字条 / 她那栋楼
post(t) {
  const sharp = ss(seg(t, T.walker - 1.2, T.walker - .2)) * (1 - ss(seg(t, T.stars - 1.4, T.stars - .4)));
  return { focus: S.cam.position.z - focusZ, aper: 16 - 12 * sharp, maxCoc: 12, bloom: { strength: .34 - .12 * sharp, radius: .58, threshold: 1.18 } };
},
```

### 3.7 会发光的字和线（`film.js` 第 48–52、235、261–266 行）

- 发光图（`glowDraw`）只在纸不透明的地方生效。字、线在纸上画成**浅色实体**，发光图里画成**黑底白形**（SHORTS.md §4）。挖空（`destination-out`）的地方被 alphaTest 丢掉，就亮不起来了。
- 用在两个气泡（`bubble()`）、名字条、星座、心、纸灯。星座用引擎自带的圆形裁剪 `uClip` 揭开。
- 纸上的字只在建层时画一次，所以 `main.js` 在 `build()` 之前先 `document.fonts.load`；气泡里有拉丁字母，另外预载了 600 字重。

```js
function bubble(x, w, h, tail, s, size, font, glow) {
  if (glow) { x.fillStyle = '#000'; x.fillRect(-w, -h, w * 2, h * 2); text(x, s, 0, .002, size, font, { fill: '#fff', weight: 600 }); return; }   // 黑底白字
  x.fillStyle = '#1c1426'; x.beginPath(); x.roundRect(-w / 2, -h / 2 + .004, w, h - .004, .006); x.fill();   // 深色纸（…尾巴）
  text(x, s, 0, .002, size, font, { fill: '#f7e3bd', weight: 600 });            // 浅色实字，不挖空
}
STARS.forEach(([px, py], i) => { if (!i) g.moveTo(px, py); else { const [, qy] = STARS[i - 1]; g.lineTo(px, qy); g.lineTo(px, py); } });   // 先横后竖 = 电路
// update：以第一颗星为圆心，半径 0 → .16 m；uClip.w = 0 表示只留圈内
stars.material.userData.u.uClip.value.set(STARS[0][0], STARS[0][1], .16 * ss(seg(t, T.stars, T.stars1)), 0);
```

### 3.8 高潮的光、纸灯和雨（`film.js` 第 118–121、205–207、224–225、238–243 行）

- 一个 `boost`（1 → 1.9，63.99 s 起增量回落 35%）同时推三处：她的窗、整箱背光 `uLit`、桌面溢光 `spill`。冷光窗同时压暗 85%。
- 纸灯三层（9 / 8 / 6 盏），越近走得越快（6.5 / 5.5 / 4.5 s 走完 .7 m），自带视差。
- 雨只下左右两条（|x| .075–.178）。每滴按 .06 m 周期画 9 遍，整张纸按同一周期取模下移，循环不跳（SHORTS.md §6）。

```js
const boost = 1 + .9 * ss(seg(t, T.lan, T.lan + 2.2)) * (1 - .35 * ss(seg(t, T.lan1, T.lan1 + 2)));
building.material.userData.u.uGlowLit.value = ss(seg(t, T.winOn, T.winOn + .5)) * (1 + .03 * Math.sin(t * 5.1)) * boost;
U.uLit.value = 1 + .25 * (boost - 1);                                                    // 整箱背光
R.spill.intensity = 6 * lamp * (1 + .03 * Math.sin(t * 5.3)) * (1 + .3 * (boost - 1));  // 桌面溢光
lan.forEach((m, i) => { const k = (t - T.lan) / (6.5 - i); m.visible = k > 0 && k < 1.2; m.position.y = lerp(-.34, .36, k); /* … */ });
// 雨：rainDraw 里每滴画在 py = -FH / 2 + py0 + k * .06（k = 0…8）
for (const r of [rainL, rainR]) { r.visible = rk > 0; r.material.color.setScalar(rk); r.position.y = -((t * .09) % .06); }
```

## 4. 声音

- **配音**：本地 VoxCPM2（讲解口吻音色），一句一场地配，导入、挂字见 SHORTS.md §3。
  - 句间 `GAP` .35–1.1 s；纸灯那句后留 1.6 s；最后一句后留 8.6 s。
  - 配音工具把 L14 标了「异常」（2.7 字/秒），自动换种子重配成 4.32 s。
  - `voices/L15.wav` 是删掉的结尾句，留着不用（`main.js` 只遍历 `LINES`）。
- **配乐**：'Echoes Of Home'，Scott Buckley，CC BY 4.0，291.7 s，在 demo 素材包里（`styles/paper-lantern/demo/music/sb_EchoesOfHome.mp3`）。`MUSIC.md` 记着它是一条没有鼓的长渐强。
  - 起点倒着算：按 2 s 窗口量整首的 RMS，最响在 146 s；要它落在名字条（片中 68 s），起点 = 146 − 68 = 78 s。高潮（片中 55.6 s）正好进入曲中 134–172 s 的最强段。
  - 开头 3.5 s 淡入（曲线 ^1.5），尾 4 s 淡出。
  - 署名按作者指定格式：`'Echoes Of Home' by Scott Buckley - released under CC-BY 4.0. www.scottbuckley.com.au`（`MUSIC.md`）。片尾小字带网址；发文正文只写曲名、作者和许可，不带网址（SHORTS.md §7）。
- **拟音**：`mix.py` 现合成 14 类，按 `EV` 放，增益表 `G`（线性 .1–.5）。比如翅膀是 14 Hz 门控噪声；玩偶 pop 每个隔 .22 s，声像左右排开；脚步每 .42 s 一下；星星是 6 个上行铃。
- **电平**（最终版 `mix.py` 报告）：
  - 人声：压缩（阈值 .28 线性、3:1）+ 高通 70 Hz，说话段 RMS −18.0 dB。
  - 配乐：先归一到 −27 dB RMS，说话时再压 5.5 dB（包络 .25 s 平滑、×1.6），整轨实测 −30.5 dB。拟音说话时压 4 dB；每声道限幅 .95。
  - 分段 RMS：开灯 −26.2、守护 −18.7、高潮 −18.1、点题 −17.9、桌前 −25.1 dB。mux 用 `LUFS=-16`。

## 5. 竖版改造

- 灯箱、相机、后期照 SHORTS.md §2：`room.js` 的 `BOX` 改 .36×.48；`stage.js` 相机 aspect 3/4，默认 fov 26 → 34；`post.js` 的 `aspect` 改 3/4（只影响 iris 转场，本片没用上）。
- 满幅纸 `.358×.478`，比内腔小 2 mm（STYLE.md §3：纸比内腔大会从木框里穿出来）。
- 画布：`main.js` 里 `setSize(1080, 1440)`、`new Pipe(renderer, 1080, 1440, SSAA)`；`index.html` 的 `#c` 和 `render/page.mjs` 的视口都是 1080×1440。字幕 `#sub` 离底 96 px、左右各 40 px、42 px 字（SHORTS.md §1）；`#credit` 离底 46 px、19 px。
- 片子目录**没有** `size.json`，因为本片用自己的 `render/`（写死竖版）。改用 `core/render` 要先补上（SHORTS.md §1）。
- 构图：上面约三分之一是天（月亮左上、星座右上、竖排片名在左）；中间是她那栋楼，窗在正中偏下；下面是街。
  - 街面从 −.21 抬到 `GROUND = −.17`，街上的人和门都在字幕带之上。
  - 名字条在最底（y −.226），满框时落在画面底部 96 px 里。私人片无所谓，发平台的要上移。
- 桌上道具：`room.js` 删了茶具和月饼（连带去掉对 `shots/s03_press.js` 的 import，本片没有 `shots/`），换成一部手机（第 48–62 行）：

```js
const sc = paint(.07, .15, x => { /* …底色、橙色画面 */
  text(x, '<直播间名>', 0, -.033, .0068, 'NotoSerifSC', { fill: '#fff4e2', weight: 600 });   // 米制画布写字走 text()
  /* …红点 +「直播中」 */ }, 6000);
const screen = new THREE.Mesh(new THREE.PlaneGeometry(.068, .146),
  new THREE.MeshBasicMaterial({ map: tex(sc), color: new THREE.Color(1, 1, 1).multiplyScalar(1.4) }));   // >1 才进辉光
screen.rotation.x = -Math.PI / 2; screen.position.y = .0031;   // 平躺在机身上；旁边另有一盏 .05 的暖色点光
```

## 6. 封面

- **干净帧**：`node films/<礼物片>/render/still.mjs 70 --out <目录> --q '?ssaa=2&nosub'` → `cover.jpg`。
  - 选 70 s：满框，七位都在，纸灯已经飞走，名字条亮着，片尾署名还没出来。点题句的字幕这时还在，用 `?nosub` 关掉（`main.js` 第 46 行）。
- **大字封面**（`cover-大字.jpg`）：让 Codex CLI 拿上面那帧当参考生图。在空的临时目录里跑，参考帧先拷进去：

```
codex exec --skip-git-repo-check --ephemeral -s workspace-write -C <临时目录> \
  -c model_reasoning_effort='"high"' -i <临时目录>/ref-frame.jpg -o <临时目录>/last.txt - < prompt.md
```

- prompt 里写死：参考帧里每个元素是什么；大字逐字写出、分几行、哪个词最大最亮；成品 1080×1440 JPG 和文件名；场景和剪影不许变形、不许换画风；底部名字条要么一字不差，要么整行去掉；大字放在夜空，每字至少 120 px 高，别挡亮窗。
  - 还要写：生成后自己放大检查，最多 3 次，不行就用 PIL 加片里的字体把字排到参考帧上；只准写当前目录。
- 结果：生成 2 次，用第 2 版，前后约 3 分钟。Codex 自己去掉了名字条和竖排片名给大字腾地方。当时走 Codex 自带生图，不另外按张计费；换环境先确认计费。
- **逐字核对**：用 PIL 裁出标题区 `(100, 50, 1000, 480)` 和场景区 `(80, 560, 740, 1260)`，放大逐字看笔画，逐个对剪影，跟原帧一致才用。
- 交付：私人片按「文件」发，微信直接发视频会压画质（`文案.md`）。

## 7. 返工记录

1. **写完、渲之前自查**：
   - 星座那张纸是透明的，线只画进了发光图，alphaTest 把整张丢了。改成纸上也画浅色线。
   - 气泡字挖空了不亮，改成浅色实字（§3.7）。雨是随机撒点，循环会跳，改成周期平铺（§3.8）。
   - 手机屏直接写 `x.font = '600 .0072px …'`，米制画布里字号太小画不出来。改走 `text()`：先缩 .001，字号 ×1000。
   - 翅膀纸只有 .04 宽，扇的时候被裁，加到 .06。会转的部件，纸要留出它扫过的范围。
2. **页面 180 s 不就绪**：几行 `add({…})` 后面多写了一个 `)`。脚本自动修只修了两处；`.map(` 包着的玩偶那行反而需要 `}));`。本片 `render/page.mjs` 只打印 `[pageerror]`，照样等满 180 s。
   - 教训：渲之前先 `node --check films/<名>/src/*.js`（仓库 `package.json` 是 `"type": "module"`，直接按 ES module 查）。看到 `[pageerror]` 就停。
3. **首批静帧**：窗纸画成暖黄，开灯前就像亮着。改成暗色 `#6a5a4a`，亮全靠发光图。手机出了画，挪到 (.215, .13)。
4. **18 张静帧拼成总览图**：
   - 鸟没出现：同一句里一个字出现两次（SHORTS.md §3 那个例子），取了第一次。落地时刻 22.82 早于起飞 22.94，`seg()` 夹成 0，鸟一直停在画外的起点。
   - 查法：临时加 `window.DBG = { bird, … }`，用 `page.evaluate` 在 27.2 s 把 `visible/position/scale` 打出来。
   - 街上的人被字幕挡住，街面抬到 −.17。门口那个气泡一直不收，`pop()` 补上收的时刻 `t1`。
5. **镜头一直在滑**，人说话时被挤出画。改成到位、停住、提前 1 s 起步（§3.5）。
6. **第一版成片抽帧**（ffmpeg 抽 18 帧，另裁 y 1040–1440 的字幕带单看）：
   - 门口的人是一坨又高又黑的影子，头跟玩偶糊在一起；提灯的人像积木人。重刻剪影（§3.3），定妆页过两轮，第二轮给提灯的人加长外套、腿加粗。
   - 中间版为了看清把人放大到约 .09 m，是门高（.042 m）的两倍多，像巨人。缩回真人比例，镜头推到 z .29 / .22。
   - 缩回来以后细剪影被亮门、亮窗洗白，按拍收光圈、减辉光（§3.6）。
   - 字幕压在亮门上看不清，`text-shadow` 改成 5 层，加了 2 / 5 / 9 px 三层贴字的深色晕当描边。
7. **改一句台词**（按要求删掉一句介绍词里的个人信息）：只重配 L07，4.32 → 3.52 s。省下的 0.8 s 拆给 `GAP.L06`（+.3）和 `GAP.L07`（+.5），L08 以后一格不动（SHORTS.md §3）。
   - 验证：重导 `timeline.json` 跟旧版 diff，只有玩偶的 pop 从 36.04 挪到 35.22。再 grep 源码、注释、README、字体预载串，确认旧词清干净。
8. **删结尾一句**：原来结尾有一句做片人署名式的旁白，礼物片片尾不署做片人的名（SHORTS.md §8），删了。
   - `LINES` 删行，`GAP.L14` 1.4 → 8.6。`T.out` 从挂 `C.L15.at − .8` 改挂 `C.L14.end + .6`，数值不变（71.65）。
   - 片尾署名从挂 `C.L15.end` 改挂 `F.T.out + 4.2`（`film.js` 把 `T` 导出给 `main.js`）。全片 80.65 → 79.65 s，配乐起点不动。
   - 教训：收尾的时刻都挂在 `T.out` 上，别挂在某一句上。

## 8. 下一期能直接拿走的

- 整个 `src/` 可以当竖版纸雕灯影的起点：`stage.js`、`post.js`、`room.js` 已是竖版；`paper.js`、`art.js`、`people.js`、`props.js`、`lib.js` 跟 demo 一字不差。
- `film.js` 的骨架照用、故事全换：`add()` 建全再藏、`T` + `events`、`beats` + `camAt()`、`show()`、`pop()`、`bubble()`、`lanterns()`、`skyline()`。
- `main.js`：单场景渲染循环（没有镜头调度和叠化），带 `at()`、字幕 15 字断行、`?nosub`，署名挂 `F.T.out`。要多镜头叠化，回 demo 的 `main.js` 拿调度器。
- `figures.js` 学写法，人物本身别复用；`sheet.html` + `render/sheet.mjs` 换人物就能用；`render/timeline.mjs` + `mix.py` 换曲只改文件和起点。
- 本片 `render/`（demo 那套改的）和 `core/render/` 的区别：

| | 本片 `render/` | `core/render/` |
|---|---|---|
| 调用 | `node films/<名>/render/video.mjs …`，脚本自己认片子目录 | `node core/render/video.mjs films/<名> …` |
| 画幅 | 写死 1080×1440 | 读 `size.json`，没有就是 1920×1080 |
| 页面报错 | 只打印 `[pageerror]`，照等 READY 180 s | 立刻退出，返回非 0 |
| `--q` | 要带 `?`：`--q '?ssaa=1'` | 不带：`--q 'ssaa=1'` |
| 视频默认 | 30 fps、6 路、crf 12，支持 `--from/--to` | 24 fps、3 路、crf 14 |
| 另有 | `timeline.mjs`（→ `timeline.json`）、`sheet.mjs` | `events.mjs`（→ `events.json`）、`still.mjs --range`、`sheet.py`、`mux.sh` |

- 07 期改用 `core/render` 的话：补 `size.json`，`mix.py` 改读 `events.json`；或者直接留着本片这套 `render/`。07 期还要补回 SHORTS.md §8 的系列要素：三样干货、结尾口号、片尾引擎署名、封面格式。本片是私人片，这些都没有。
- 审片节奏：`?ssaa=1` 静帧每张几十到几百毫秒，挂在每拍的关键字上出，用 PIL 拼总览图，再放大看单帧；整片渲完从 `final.mp4` 抽帧、裁字幕带，关键句用 `volumedetect` 量一下。

## 9. 本机重出

在仓库根下跑。`films/` 不在 git 里，源码只在我的 Mac 上。

```
sh tools/fetch.sh demo paper-lantern      # 字体和配乐在 demo 素材包里（83 MB）；木纹贴图 core/assets/polyhaven/ 仓库自带
node films/<礼物片>/render/timeline.mjs && .venv/bin/python films/<礼物片>/mix.py
node films/<礼物片>/render/video.mjs --fps 30 --workers 4 --out films/<礼物片>/out/video.mp4
LUFS=-16 sh core/render/mux.sh films/<礼物片>/out/video.mp4 films/<礼物片>/mix.wav films/<礼物片>/out/final.mp4 30 0
```

- 看静帧：`node films/<礼物片>/render/still.mjs 10 36 58.6 69.6 --out <目录> --q '?ssaa=1'`；定妆页：`node films/<礼物片>/render/sheet.mjs <输出.jpg>`
- 依赖：稀疏检出里要有 `/styles/paper-lantern/`；`node_modules`（three 0.170、playwright-core）；`.venv`（numpy、soundfile、soxr、scipy）；ffmpeg。
- 配音 WAV 和逐字时间都在 `voices/`，重出不用再配音。成片只存成片盘，`out/` 入盘后进废纸篓（SHORTS.md §7）。
