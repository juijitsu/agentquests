/* Прогресс и замки. Хранится у посетителя, считается на клиенте.

   Правило одно на весь курс: первый уровень трека открыт всегда, каждый
   следующий открывает пройденный предыдущий. Треки друг друга не запирают —
   заходить в «Контекст» вместо «Фундамента» разрешено, и пройти его можно
   целиком. Порядок внутри трека остаётся обязательным: там уровень честно
   опирается на предыдущий.

   Замки здесь — вежливость, а не охрана: прогресс лежит у ученика в браузере.
   Держать оборону на статическом сайте не на чем, а списывать у самого себя
   незачем.

   Под тем же ключом теперь лежит не список пройденных, а карта записей: к
   «пройден» добавились число попыток, время и то, что не сошлось в последний
   раз. Ключ тот же намеренно — у людей уже есть прогресс, и терять его
   нельзя; старая форма читается и переводится в новую при первом чтении.

   `readDone()` возвращает то же, что и раньше, поэтому замки, `Gate` и
   `blockedBy` не тронуты вовсе. */

import type { Lang } from "@/lib/i18n";

export const DONE_KEY = "aq-done";

export type Outline = { track: string; levels: string[] }[];

/** Запись об уровне. Ключ карты — id уровня, «red-team/01-attack-surface». */
export type Mark = {
  /** Засчитанных прогонов: и сдача, и несовпадение. Прерванные не в счёт. */
  runs: number;
  /** Когда был последний засчитанный прогон. Нет — запись пришла из старой формы. */
  at?: number;
  /** Сдан. С этой минуты запись не меняется. */
  done?: true;
  /** Строки «✗» последнего несошедшегося прогона. Со сдачей исчезают. */
  miss?: string[];
};

export type Marks = Record<string, Mark>;

/* Самый длинный вердикт в курсе — шесть условий (04-evaluation/08-boss),
   посчитано по всем сценариям. Ограничение стоит против будущего уровня, а
   не режет существующие. */
const MISS_LINES = 6;
const MISS_CHARS = 120;

const EMPTY: Marks = {};
let cache: Marks | null = null;
const watching = new Set<() => void>();

function parse(raw: string): Marks {
  const value: unknown = JSON.parse(raw);
  // Старая форма — просто список пройденных. Ни числа попыток, ни времени у
  // них нет и взяться неоткуда, поэтому запись выходит короткой.
  if (Array.isArray(value)) {
    const marks: Marks = {};
    for (const id of value as string[]) marks[id] = { runs: 0, done: true };
    return marks;
  }
  return (value ?? {}) as Marks;
}

/** Карта записей. Один и тот же объект между записями: его читает подписка. */
export function readMarks(): Marks {
  if (cache) return cache;
  try {
    const raw = localStorage.getItem(DONE_KEY);
    cache = raw ? parse(raw) : EMPTY;
  } catch {
    cache = EMPTY;
  }
  return cache;
}

/** На сервере прогресса нет: там всегда пусто, и это стабильный объект. */
export function noMarks(): Marks {
  return EMPTY;
}

export function watchMarks(notify: () => void): () => void {
  watching.add(notify);
  return () => {
    watching.delete(notify);
  };
}

export function readDone(): string[] {
  const marks = readMarks();
  return Object.keys(marks).filter((id) => marks[id].done);
}

function missFrom(output: string): string[] {
  return output
    .split("\n")
    .map((line) => line.trim())
    .filter((line) => line.startsWith("✗"))
    .map((line) => line.slice(1).trim().slice(0, MISS_CHARS))
    .slice(0, MISS_LINES);
}

/** Итог прогона. Зовётся один раз на завершённый прогон, из Runner. */
export function saveRun(levelId: string, code: number, output: string): Marks {
  const marks = readMarks();
  const was = marks[levelId];

  // Прерванный вручную прогон и сбой воркера попыткой не считаются: ученик
  // ничего не проверял.
  if (code === 2) return marks;
  // Сдан — запись больше не меняется, иначе «сдан 4 сентября» однажды станет
  // неправдой.
  if (was?.done) return marks;

  const runs = (was?.runs ?? 0) + 1;
  const now = Date.now();
  const next: Mark =
    code === 0 ? { runs, at: now, done: true } : { runs, at: now, miss: missFrom(output) };

  cache = { ...marks, [levelId]: next };
  try {
    localStorage.setItem(DONE_KEY, JSON.stringify(cache));
  } catch {
    /* приватный режим — прогресс просто не сохранится */
  }
  for (const notify of watching) notify();
  return cache;
}

/** «4 сентября», а год — только если он не нынешний. */
export function whenText(at: number, lang: Lang): string {
  const date = new Date(at);
  const sameYear = date.getFullYear() === new Date().getFullYear();
  return date.toLocaleDateString(lang === "ru" ? "ru-RU" : "en-GB", {
    day: "numeric",
    month: "long",
    ...(sameYear ? {} : { year: "numeric" }),
  });
}

export function levelOpen(outline: Outline, levelId: string, done: string[]): boolean {
  return blockedBy(outline, levelId, done) === null;
}

/** Что именно надо пройти, чтобы открылось. Для понятного сообщения. */
export function blockedBy(
  outline: Outline,
  levelId: string,
  done: string[],
): string | null {
  const track = outline.find((t) => t.levels.includes(levelId));
  if (!track) return null;
  const at = track.levels.indexOf(levelId);
  if (at <= 0) return null;
  const previous = track.levels[at - 1];
  return done.includes(previous) ? null : previous;
}
