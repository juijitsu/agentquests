/* Прогресс и замки. Хранится у посетителя, считается на клиенте.

   Правило одно на весь курс: первый уровень трека открыт всегда, каждый
   следующий открывает пройденный предыдущий. Треки друг друга не запирают —
   заходить в «Контекст» вместо «Фундамента» разрешено, и пройти его можно
   целиком. Порядок внутри трека остаётся обязательным: там уровень честно
   опирается на предыдущий.

   Замки здесь — вежливость, а не охрана: прогресс лежит у ученика в браузере.
   Держать оборону на статическом сайте не на чем, а списывать у самого себя
   незачем. */

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
