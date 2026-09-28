// 打开 demo 页面（仓库根为静态服务根），等待 window.READY
import { chromium } from 'playwright-core';
import path from 'path'; import fs from 'fs'; import { fileURLToPath } from 'url';
import { serve, pageURL } from './serve.mjs';
import { EXE, ARGS } from './browser.mjs';
export const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
let srv = null;
export async function server() { if (!srv) srv = await serve(ROOT); return srv; }
// MBP-短片 2026-09-27：片子目录里有 size.json（{"w":1080,"h":1440}）就按它的画幅渲，没有照旧 1920×1080
export function sizeOf(dir) { try { const s = JSON.parse(fs.readFileSync(path.resolve(ROOT, dir, 'size.json'), 'utf8')); return [s.w, s.h]; } catch { return [1920, 1080]; } }
export async function openDemo(dir, { w, h, q = '' } = {}) {
  if (!w || !h) [w, h] = sizeOf(dir);
  const { port } = await server();
  const browser = await chromium.launch({ executablePath: EXE, args: ARGS });
  const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
  page.on('console', m => { if (m.type() === 'error' && !m.text().includes('404')) console.error('[page]', m.text().slice(0, 300)); });
  page.on('pageerror', e => { console.error('[pageerror]', e.message); process.exit(1); });   // 渲染中报错就停，免得产出坏片
  await page.goto(pageURL(ROOT, port, dir) + (q ? '?' + q : ''));
  await page.waitForFunction(() => window.READY === true, null, { timeout: 180000 });
  return { browser, page };
}
export function closeServer() { if (srv) srv.server.close(); }
