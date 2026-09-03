/* Кладёт рантайм Python рядом с сайтом.

   Сторонний CDN в проде — чужая зависимость, которая однажды отвалится:
   в исследовании доставки ровно так закрылся бесплатный API Piston.
   Плюс воркеру нельзя грузить скрипт с чужого origin. */

import { copyFileSync, mkdirSync, existsSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const from = join(here, "..", "node_modules", "pyodide");
const to = join(here, "..", "public", "pyodide");

// Только то, что нужно рантайму: без карт, деклараций и демо-страниц.
const FILES = [
  "pyodide.mjs",
  "pyodide.asm.mjs",
  "pyodide.asm.wasm",
  "python_stdlib.zip",
  "pyodide-lock.json",
];

mkdirSync(to, { recursive: true });

let bytes = 0;
for (const name of FILES) {
  const src = join(from, name);
  if (!existsSync(src)) {
    console.error(`нет файла ${name} — проверьте, что пакет pyodide установлен`);
    process.exit(1);
  }
  copyFileSync(src, join(to, name));
  bytes += (await import("node:fs")).statSync(src).size;
}

console.log(`pyodide: ${FILES.length} файлов, ${(bytes / 1e6).toFixed(1)} МБ → public/pyodide`);
