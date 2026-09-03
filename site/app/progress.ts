/* Прогресс и замки. Хранится у посетителя, считается на клиенте.

   Правило простое и одно на весь курс: следующий уровень открывает
   пройденный предыдущий, следующий трек — пройденный целиком предыдущий. */

export const DONE_KEY = "aq-done";

export type Outline = { track: string; levels: string[] }[];

export function readDone(): string[] {
  try {
    const raw = localStorage.getItem(DONE_KEY);
    return raw ? (JSON.parse(raw) as string[]) : [];
  } catch {
    return [];
  }
}

export function saveDone(levelId: string): string[] {
  const done = readDone();
  if (done.includes(levelId)) return done;
  const next = [...done, levelId];
  try {
    localStorage.setItem(DONE_KEY, JSON.stringify(next));
  } catch {
    /* приватный режим — прогресс просто не сохранится */
  }
  return next;
}

export function trackOpen(outline: Outline, at: number, done: string[]): boolean {
  if (at <= 0) return true;
  return outline
    .slice(0, at)
    .every((t) => t.levels.every((id) => done.includes(id)));
}

export function levelOpen(outline: Outline, levelId: string, done: string[]): boolean {
  const at = outline.findIndex((t) => t.levels.includes(levelId));
  if (at < 0) return true;
  if (!trackOpen(outline, at, done)) return false;
  const inside = outline[at].levels.indexOf(levelId);
  if (inside <= 0) return true;
  return done.includes(outline[at].levels[inside - 1]);
}

/** Что именно надо пройти, чтобы открылось. Для понятного сообщения. */
export function blockedBy(
  outline: Outline,
  levelId: string,
  done: string[],
): string | null {
  const at = outline.findIndex((t) => t.levels.includes(levelId));
  if (at < 0) return null;
  for (let i = 0; i < at; i++) {
    const missing = outline[i].levels.find((id) => !done.includes(id));
    if (missing) return missing;
  }
  const inside = outline[at].levels.indexOf(levelId);
  if (inside > 0 && !done.includes(outline[at].levels[inside - 1])) {
    return outline[at].levels[inside - 1];
  }
  return null;
}
