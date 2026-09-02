/**
 * Раннер уровней на TypeScript. Двойник engine/check.py по контракту:
 * тот же вывод, те же коды возврата.
 *
 *     node engine/check.mjs <путь к agent.ts>
 *
 * Отдельную команду учить не нужно: check.py вызывает этот файл сам,
 * увидев расширение решения. Типы снимает сам Node — сборки нет.
 */

import { existsSync } from "node:fs";
import { basename, dirname, join, resolve } from "node:path";
import { pathToFileURL } from "node:url";

const OK = "✓";
const NO = "✗";

function findLevel(start) {
  for (let dir = start; ; ) {
    if (existsSync(join(dir, "scenario.ts"))) return dir;
    const up = dirname(dir);
    if (up === dir) return null;
    dir = up;
  }
}

const load = (path) => import(pathToFileURL(path).href);

async function main() {
  const given = process.argv[2];
  if (!given) {
    console.log("укажите путь к решению");
    return 2;
  }

  const agentPath = resolve(given);
  if (!existsSync(agentPath)) {
    console.log(`FAIL  файла нет: ${agentPath}`);
    return 1;
  }

  const levelDir = findLevel(dirname(agentPath));
  if (levelDir === null) {
    console.log("FAIL  рядом с решением не найден scenario.ts");
    return 2;
  }

  const scenario = await load(join(levelDir, "scenario.ts"));

  console.log(`\n  ${scenario.TITLE}`);
  console.log(`  ${basename(agentPath)} · ${basename(dirname(agentPath))}\n`);

  if (scenario.BRIEF) {
    for (const line of scenario.BRIEF.trim().split("\n")) console.log("  " + line);
    console.log();
  }

  let result;
  try {
    result = scenario.play(await load(agentPath));
  } catch (exc) {
    if (exc?.name === "NotImplemented") {
      console.log(`  ${NO} run() ещё не реализована`);
      console.log("\n  FAIL  Это заготовка для сложности «профессионал».");
      console.log("        Соберите решение сами или возьмите starter/advanced.\n");
      return 1;
    }
    const hint = scenario.explain ? scenario.explain(exc) : null;
    console.log(`  ${NO} решение упало: ${exc?.name ?? "Error"}`);
    if (hint) {
      console.log(`\n  FAIL  ${hint}\n`);
    } else {
      console.log();
      console.error(exc);
      console.log();
    }
    return 1;
  }

  if (!Array.isArray(result) || result.length !== 2) {
    console.log(`  ${NO} run() вернула не кортеж (ответ, число итераций)`);
    console.log("\n  FAIL  Посмотрите контракт run() в шапке файла.\n");
    return 1;
  }

  const verdicts = scenario.verify(result);
  const ok = verdicts.every(([passed]) => passed);
  for (const [passed, message] of verdicts) {
    console.log(`  ${passed ? OK : NO} ${message}`);
  }

  console.log("\n  " + (ok ? "PASS  следующий уровень открыт\n" : "FAIL\n"));
  return ok ? 0 : 1;
}

process.exit(await main());
