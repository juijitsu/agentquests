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

// Вердикт читает ученик, поэтому он идёт на языке уровня. Язык называет сам
// сценарий — как и в check.py, умолчание русское.
const SAYS = {
  ru: {
    notImpl: "run() ещё не реализована",
    notImplWhy: "Это заготовка для сложности «профессионал».",
    notImplHow: "Соберите решение сами или возьмите starter/advanced.",
    crashed: "решение упало",
    badType: "run() вернула не кортеж (ответ, число итераций)",
    badTypeHow: "Посмотрите контракт run() в шапке файла.",
    pass: "PASS  следующий уровень открыт",
    fail: "FAIL",
  },
  en: {
    notImpl: "run() is not implemented yet",
    notImplWhy: "This is the starter for the pro tier.",
    notImplHow: "Build the solution yourself or take starter/advanced.",
    crashed: "the solution crashed",
    badType: "run() did not return a tuple (answer, iterations)",
    badTypeHow: "Check the run() contract at the top of the file.",
    pass: "PASS  the next level is open",
    fail: "FAIL",
  },
};

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
  const says = SAYS[scenario.LANG] ?? SAYS.ru;

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
      console.log(`  ${NO} ${says.notImpl}`);
      console.log(`\n  ${says.fail}  ${says.notImplWhy}`);
      console.log(`        ${says.notImplHow}\n`);
      return 1;
    }
    const hint = scenario.explain ? scenario.explain(exc) : null;
    console.log(`  ${NO} ${says.crashed}: ${exc?.name ?? "Error"}`);
    if (hint) {
      console.log(`\n  ${says.fail}  ${hint}\n`);
    } else {
      console.log();
      console.error(exc);
      console.log();
    }
    return 1;
  }

  if (!Array.isArray(result) || result.length !== 2) {
    console.log(`  ${NO} ${says.badType}`);
    console.log(`\n  ${says.fail}  ${says.badTypeHow}\n`);
    return 1;
  }

  const verdicts = scenario.verify(result);
  const ok = verdicts.every(([passed]) => passed);
  for (const [passed, message] of verdicts) {
    console.log(`  ${passed ? OK : NO} ${message}`);
  }

  console.log("\n  " + (ok ? says.pass + "\n" : says.fail + "\n"));
  return ok ? 0 : 1;
}

process.exit(await main());
