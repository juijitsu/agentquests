import type { Dict } from "@/lib/i18n";

/* Питон объясняет ошибку по-английски и по-своему: «expected ':'», «'(' was
   never closed». Новичку это ничего не говорит, а если он не знает
   английского — не говорит вдвойне.

   Сопоставляем по тексту самого питона, а не по нашим догадкам о коде.
   Текст питона от языка интерфейса не зависит, поэтому правила одни на оба
   языка, а человеческие фразы берутся из словаря.

   Железное условие ко всему файлу: **каждое правило доказуемо из фактов** —
   из текста исключения, из вердикта или из самого кода ученика. Совет,
   выданный наугад, для новичка хуже молчания. */

export type Problem = {
  line: number;
  column: number;
  message: string;
};

export type Hint = { title: string; body: string; html?: boolean };

const SYNTAX: { has: RegExp; key: keyof Dict["live"] }[] = [
  { has: /was never closed/i, key: "unclosed" },
  { has: /unterminated triple-quoted string/i, key: "unterminatedTriple" },
  { has: /unterminated string literal/i, key: "unterminatedString" },
  { has: /expected ':'/i, key: "colon" },
  { has: /expected an indented block/i, key: "needIndent" },
  { has: /unexpected indent/i, key: "extraIndent" },
  { has: /unindent does not match/i, key: "mixedIndent" },
  { has: /inconsistent use of tabs/i, key: "tabs" },
  { has: /'return' outside function/i, key: "returnOutside" },
  { has: /cannot assign to/i, key: "assignTo" },
  { has: /invalid character/i, key: "invalidChar" },
  { has: /leading zeros in decimal/i, key: "leadingZero" },
  { has: /perhaps you forgot a comma/i, key: "missingComma" },
];

/** Человеческое объяснение синтаксической ошибки, или null, если её нет. */
export function explainSyntax(
  name: string,
  message: string,
  dict: Dict,
): string | null {
  if (!name) return null;
  if (name === "TabError") return dict.live.tabs;
  const rule = SYNTAX.find((r) => r.has.test(message));
  if (rule) return dict.live[rule.key];
  if (name === "IndentationError") return dict.live.needIndent;
  // Правила не нашлось — отдаём общее объяснение и слова самого питона:
  // лучше показать непонятное, чем промолчать о поломке.
  return `${dict.live.generic} ${message}`.trim();
}

/* Имя класса исключения питон печатает по-английски всегда, независимо от
   языка страницы, поэтому его и ищем — а не переведённую подпись движка. */
const CRASH = /^([A-Za-z_][A-Za-z0-9_]*(?:Error|Exception)): ?(.*)$/gm;

function lastCrash(output: string): { name: string; message: string } | null {
  const all = [...output.matchAll(CRASH)];
  const last = all[all.length - 1];
  return last ? { name: last[1], message: (last[2] ?? "").trim() } : null;
}

/** Что делать с исключением, которое случилось уже при запуске. */
export function explainRuntime(name: string, dict: Dict): string {
  const table = dict.star.runtime as Record<string, string>;
  return table[name] ?? table.generic;
}

const DEF = /^[ \t]*def[ \t]+([A-Za-z_][A-Za-z0-9_]*)/gm;

function definedIn(source: string): string[] {
  return [...source.matchAll(DEF)].map((m) => m[1]);
}

/** Заметки, которые видно прямо в коде ученика. Каждая — факт, а не догадка.
    `said` — объяснение самого уровня: если оно уже назвало ту же вещь,
    повторять её другими словами значит набивать подсказки. */
function codeNotes(
  code: string,
  starter: string,
  tier: string,
  said: string,
  dict: Dict,
): Hint[] {
  // Код не тронут вовсе — остальные замечания к нему бессмысленны.
  if (code.trim() === starter.trim()) {
    return [{ title: dict.star.noteTitle, body: dict.star.untouched }];
  }

  const notes: Hint[] = [];
  const wanted = definedIn(starter);
  const have = new Set(definedIn(code));
  const lost = wanted.find((name) => !have.has(name));
  if (lost && !said.includes(lost)) {
    notes.push({ title: dict.star.noteTitle, body: dict.star.renamed(lost) });
  }

  // Печать вместо возврата: ловим только когда return не встречается вообще,
  // иначе это была бы догадка о том, какая ветка сработает.
  if (/\bprint\s*\(/.test(code) && !/\breturn\b/.test(code)) {
    notes.push({ title: dict.star.noteTitle, body: dict.star.printNoReturn });
  }

  if (tier === "novice" && starter.includes("TODO") && code.includes("TODO")) {
    notes.push({ title: dict.star.noteTitle, body: dict.star.todoLeft });
  }

  return notes.slice(0, 2);
}

/** Всё, что звезда знает про положение дел, в порядке от частного к общему. */
export function starHints(input: {
  output: string;
  verdict: number | null;
  code: string;
  starter: string;
  tier: string;
  hasNovice: boolean;
  levelHint: string;
  problem: Problem | null;
  dict: Dict;
}): Hint[] {
  const { output, verdict, code, starter, tier, hasNovice, levelHint, problem, dict } = input;

  if (verdict === 0) {
    return [{ title: dict.hDoneTitle, body: dict.hDoneBody }];
  }

  const lines = output.split("\n").map((l) => l.trim());
  const failed = lines.filter((l) => l.startsWith("✗")).map((l) => l.slice(1).trim());

  // Объяснение движка занимает несколько строк: заголовок FAIL и перенос
  // фразы под ним. Взять одну строку — значит оборвать её на полуслове.
  const at = lines.findIndex((l) => l.startsWith("FAIL"));
  let said = "";
  if (at >= 0) {
    const block = [lines[at].replace(/^FAIL\s*/, "")];
    for (let i = at + 1; i < lines.length && lines[i]; i++) block.push(lines[i]);
    said = block.join(" ").trim();
  }

  const hints: Hint[] = [];

  // Синтаксис виден до всякого запуска, и пока он сломан остальное неважно.
  if (problem) {
    hints.push({
      title: dict.star.syntaxTitle,
      body: `${dict.liveAt(problem.line)}. ${problem.message}`,
    });
  }

  if (verdict === null) {
    if (!problem) hints.push({ title: dict.hStartTitle, body: dict.hStartBody });
  } else {
    const crash = lastCrash(output);
    if (crash) {
      hints.push({
        title: dict.star.crashTitle,
        body: `${crash.name}. ${explainRuntime(crash.name, dict)}`,
      });
    } else if (failed.length > 0) {
      hints.push({
        title: failed.length === 1 ? dict.hOneFailed : dict.hManyFailed,
        body: failed.join("\n"),
      });
    } else {
      hints.push({ title: dict.hNoChecksTitle, body: dict.hNoChecksBody });
    }
    // Объяснение уровня точнее общего, поэтому идёт следом за самим фактом.
    if (said) hints.push({ title: dict.hEngineTitle, body: said });
  }

  hints.push(...codeNotes(code, starter, tier, said, dict));

  if (levelHint) hints.push({ title: dict.hLevelTitle, body: levelHint, html: true });

  hints.push({
    title: dict.hWhereTitle,
    body: (tier !== "novice" && hasNovice ? dict.hWhereNovice : "") + dict.hWhereBody,
  });

  return hints;
}
