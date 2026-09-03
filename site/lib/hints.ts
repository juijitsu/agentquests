import type { Dict } from "@/lib/i18n";

/* Питон объясняет синтаксическую ошибку по-английски и по-своему: «expected
   ':'», «'(' was never closed». Новичку это ничего не говорит, а если он не
   знает английского — не говорит вдвойне.

   Сопоставляем по тексту самого питона, а не по нашим догадкам о коде.
   Текст питона от языка интерфейса не зависит, поэтому правила одни на оба
   языка, а человеческие фразы берутся из словаря. */

export type Problem = {
  line: number;
  column: number;
  message: string;
};

const RULES: { has: RegExp; key: keyof Dict["live"] }[] = [
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

/** Человеческое объяснение синтаксической ошибки, или null, если ошибки нет. */
export function explainSyntax(
  name: string,
  message: string,
  dict: Dict,
): string | null {
  if (!name) return null;
  if (name === "TabError") return dict.live.tabs;
  const rule = RULES.find((r) => r.has.test(message));
  if (rule) return dict.live[rule.key];
  if (name === "IndentationError") return dict.live.needIndent;
  // Правила не нашлось — отдаём общее объяснение и слова самого питона:
  // лучше показать непонятное, чем промолчать о поломке.
  return `${dict.live.generic} ${message}`.trim();
}
