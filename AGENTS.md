# Lemo-Opuscar: instructions for agents

> **shorts 分支（竖版中文短视频）**：这里专门做小红书 / RedNote 竖版中文短视频。开工前先读 [`SHORTS.md`](SHORTS.md)：竖版规格、中文配音、合成配乐、各风格踩过的坑、交付规矩。

This repository is a library of film styles. Each style is a prompt (`styles/<slug>/STYLE.md`) with a demo film made entirely in code. People open an agent here, pick a style, and ask for a film about **their own** topic. Your job is to direct and produce that film.

## Read first

1. [`DIRECTOR.md`](DIRECTOR.md): how to direct (story, sound, rhythm, camera, performance, checks).
2. [`TECHNIQUE.md`](TECHNIQUE.md): how to build it (render(t) pages, voice, music, mix, review).
3. `styles/<slug>/STYLE.md` for the chosen style. §1–§8 define the style. §9 shows how our demo was built. The demo is a reference implementation: learn and reuse its techniques, but don't rebuild it or copy its story.

**The style is fixed; the content is the user's.** From a `STYLE.md`, keep the look, the motion and camera language, the sound and music, and the directing craft. The content comes from the user's topic: the story and its shape, the characters, the settings, the data and how it is charted. Many choices in a `STYLE.md` were made for our demo's story, such as a line chart for a temperature series. When one doesn't fit the user's topic, use what fits, and don't bend the topic to match the demo. The same goes for the beat tables: the story arc in §2 and the beat-by-beat camera in §5 show how our demo used the style. Read them as grammar (which kind of move serves which kind of moment), then write a new arc and shot list from the user's story.

**Finding the style.** Users name a style by its gallery name in English or Chinese ("Impasto Oil Painting", "油画厚涂") or by its folder (`impasto`). Look it up in [`styles/README.md`](styles/README.md), which maps every name to its folder. If nothing matches clearly, show the closest two or three and ask.

If the user hasn't picked a style:
- Suggest two or three that fit their topic.
- Show them the full list below in the chat, in the user's language only: English names (and English category names) for someone writing in English, Chinese names for someone writing in Chinese. Don't drop, merge or rename anything.
- Link the gallery, where every style has its demo film: https://lemomo-ai.github.io/lemo-opuscar/

<!-- style-list:start -->
All 39 styles · 全部风格:

- **手绘与绘画 Hand-drawn & Painting** (7): 蜡笔儿童绘本 Crayon Picture Book, 水彩笔刷 Watercolor Brush, 中国水墨 Chinese Ink Wash, 油画厚涂 Impasto Oil Painting, 一笔画 One-line Drawing, 白板讲解 Whiteboard Explainer, 钢笔淡彩 Urban Sketch · Pen & Wash
- **东方传统 East Asian Traditions** (4): 皮影戏 Shadow Puppetry, 浮世绘 Ukiyo-e, 红色窗花剪纸 Red Paper-cut, 纸雕灯影 Paper-cut Lightbox
- **印刷与版画 Print & Printmaking** (3): Risograph 丝网印刷 Risograph Print, 复古半调案卷 Halftone Dossier, 木刻版画 Woodcut Print
- **图形与排版 Graphic & Type** (7): 瑞士动态排版 Swiss Motion Graphics, 60s 间谍片头 60s Spy Title Sequence, 装饰艺术 Art Deco, 蓝图 / 工程制图 Blueprint, 彩色玻璃窗 Stained Glass, 象形运动图形 Pictogram Motion, ASCII / CRT 终端 ASCII / CRT Terminal
- **信息与发布 Information & Keynote** (4): 数据叙事 Data Storytelling, 等距信息图 Isometric Infographic, 暗色科技发布 Dark Tech Keynote, 活体实机录屏 Living Screencast
- **卡通与动画 Cartoon & Anime** (3): 1930s 橡皮管卡通 1930s Rubber Hose Cartoon, 80 年代赛璐璐动画 80s Cel Anime, 科幻情景喜剧卡通 Sci-Fi Sitcom Toon
- **游戏 Games** (4): 16-bit 像素 RPG 16-bit Pixel RPG, HD-2D, 微游戏快闪（瓦里奥制造式） Microgame Frenzy, 综艺节奏扁平 Game Show Flat
- **电影与时代 Cinema & Eras** (2): 1920s 默片 1920s Silent Film, 后室 / 新怪谈 Liminal Found Footage
- **材质与 3D Materials & 3D** (5): 积木玩具 Brick Toy, 纸片立体书 Paper Pop-up Book, 移轴微缩 Tilt-Shift Miniature, 低多边形等距 Low-poly Isometric Island, 玻璃质感产品 Glass Product Render
<!-- style-list:end -->

## Workflow

1. **Brief.** Make sure the style and the topic are clear. Then ask the user once, in a single message (DIRECTOR.md §1). If the style is unclear, that question goes in the same message:
   - anything about the topic you can't decide yourself (facts; names, logos or products that must appear);
   - whether they have material of their own: a voice recording or a preferred voice, music, photos, logos, fonts. Whatever they don't provide, you make;
   - whether they want to review a storyboard before production. The default is no: you go straight to the finished film.

   Skip any question their request already answers. Wait for the reply, then fill every other gap with a sensible default, sum up the brief in a few lines, and start. Don't come back with more questions later.
2. **Treatment.** Write `films/<name>/TREATMENT.md` (DIRECTOR.md §4).
3. **Look.** Render a model sheet or style frames with the real drawing code and check them yourself against the `STYLE.md` (DIRECTOR.md §5).
4. **Storyboard, only if the user asked for it.** Show the key shots rendered in the style, with durations and lines, plus the logline (DIRECTOR.md §5).
   **Stop and wait for approval.** If they didn't ask for it, don't stop.
5. **Produce.** Voice → check → score (can run in parallel) → animation → mix → render.
6. **Self-check** (DIRECTOR.md §11), then deliver `films/<name>/<name>.mp4`, `.srt`, `poster.jpg` and the source with `build.sh`.

A user's film carries no LemoLab credit and no watermark. The "LemoLab × Claude Opus 5.5" end card in the `STYLE.md` files belongs to our demos only.

Report progress in the user's language. The film's own language is whatever the user asks for (default: the language they write in).

## Where things go

- Work only in `films/<name>/` (ignored by git), unless the user asks you to work in their own project.
- `core/` has ready-made tools (rendering, TTS, speech check, sampler, sfx, mux). Use them or your own stack, but don't edit `core/` or `styles/` for a user's film.
- Large assets are fetched on demand: `sh tools/fetch.sh voice | instruments | hdri`.
- Never kill processes you didn't start. Don't leave background processes running.

## Maintaining the library (repository owner only)

To add a new style:

1. Make it in `styles/<slug>/`: `STYLE.md` in English, following the §1–§9 structure of an existing one; `TREATMENT.md`; `demo/` with the demo's source (a reference implementation, not a rebuild kit) and `CREDITS`; `<slug>.mp4`, `<slug>.srt`, `poster.jpg`, and `demo/stills/styleframe.jpg`.
2. Add a card to `styleboard/cards.json`: film title, one-line story in English and Chinese, and use cases.
3. Run `sh tools/publish.sh`. It checks the repo (no files over 5 MB, no absolute paths, no secrets), uploads new or changed films to GitHub Releases, and rebuilds the gallery data.
4. Commit and push. The gallery (GitHub Pages) rebuilds itself.

The skill in `plugin/skills/lemo-opuscar/` is a thin wrapper: it fetches this repo and sends the agent to this file. Keep the workflow here, not in `SKILL.md`.

Rules: back up before revising (old versions move out of the repo, not into git); only CC0, CC BY or OFL assets; every film's end card carries "LemoLab × Claude Opus 5.5"; no watermark.
