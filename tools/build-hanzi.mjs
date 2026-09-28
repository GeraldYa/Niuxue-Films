// 白板手写汉字库：把脚本里出现的汉字做成单线字体（EMS 同一格式：y 向上，基线 0，汉字高 880，基线下 106）。
//   node tools/build-hanzi.mjs <输出 hanzi.json> <要扫的文件…> [--data <hanzi-writer-data 目录>]
// 数据：Make Me a Hanzi 的笔画中线，按笔顺（npm hanzi-writer-data@2.0.1，Arphic Public License）。
//   默认找 films/_shared/hanzi-writer-data。取数据：
//   mkdir -p films/_shared && cd films/_shared && npm pack hanzi-writer-data@2.0.1 && tar xzf hanzi-writer-data-2.0.1.tgz && mv package hanzi-writer-data
// 片子里：await loadFont('hanzi', 'fonts/hanzi.json')，白板引擎的 text() 遇到汉字就按笔顺写。
import fs from 'fs'; import path from 'path';
const args = process.argv.slice(2), di = args.indexOf('--data');
const DATA = di >= 0 ? args.splice(di, 2)[1] : 'films/_shared/hanzi-writer-data';
const [OUT, ...FILES] = args;
if (!OUT || !FILES.length) { console.error('用法：node tools/build-hanzi.mjs <输出 hanzi.json> <要扫的文件…> [--data 目录]'); process.exit(1); }
const text = FILES.filter(f => fs.existsSync(f)).map(f => fs.readFileSync(f, 'utf8')).join('');
const chars = [...new Set(text.match(/[㐀-鿿豈-﫿]/g) || [])];
const S = 880 / 1024, DOWN = 106, glyphs = {}, miss = [];
for (const ch of chars) {
  const f = path.join(DATA, ch + '.json');
  if (!fs.existsSync(f)) { miss.push(ch); continue; }
  const j = JSON.parse(fs.readFileSync(f, 'utf8'));
  glyphs[ch] = { w: 900, s: j.medians.map(m => m.flatMap(([x, y]) => [Math.round(x * S + 10), Math.round((y + 124) * S - DOWN)])) };
}
fs.mkdirSync(path.dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, JSON.stringify({ glyphs }));
console.log(OUT, Object.keys(glyphs).length, '字', miss.length ? '缺：' + miss.join('') : '');
