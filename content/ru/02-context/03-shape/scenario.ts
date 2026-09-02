/** Третья смена трека. Те же факты, другая форма — другой ответ. */

export const TITLE = "Трек «Контекст» · Уровень 03 · Форма данных";
export const BRIEF = `Пять грузов описаны предложениями, всё подписано и на месте.
Ответ приходит про самый тяжёлый вообще, а спрашивали про сегодняшние.`;

export type Load = { id: string; tons: number; day: string };

const LOADS: Load[] = [
  { id: "TX-118", tons: 24, day: "сегодня" },
  { id: "TX-204", tons: 31, day: "завтра" },
  { id: "TX-337", tons: 27, day: "сегодня" },
  { id: "TX-441", tons: 19, day: "сегодня" },
  { id: "TX-509", tons: 22, day: "завтра" },
];

/** Так данные приходят из диспетчерской: сплошным текстом. */
export const SENTENCES: string[] = LOADS.map(
  (l) => `Груз ${l.id} весит ${l.tons} т и уезжает ${l.day}.`,
);

export const QUESTION = "Какой самый тяжёлый груз из тех, что уезжают сегодня?";
export const HEAVIEST_TODAY = "TX-337";

/** Разбирает одно предложение в запись. Работа со строкой, не с формой. */
export function parse(sentence: string): Load {
  const words = sentence.replace(".", "").split(" ");
  return { id: words[1], tons: Number(words[3]), day: words[7] };
}

export const PASSED: unknown[] = [];

function isRecords(payload: unknown): payload is Load[] {
  return (
    Array.isArray(payload) &&
    payload.length > 0 &&
    payload.every(
      (r) => r !== null && typeof r === "object" && "id" in r && "tons" in r && "day" in r,
    )
  );
}

export class Model {
  ask(question: string, payload: unknown): string {
    PASSED.length = 0;
    PASSED.push(payload);

    if (!isRecords(payload)) {
      // Из сплошного текста достаются числа, но не поля: сопоставить вес
      // с днём отправки не по чему, поэтому условие «сегодня» теряется.
      const numbers = String(payload)
        .split(" ")
        .map(Number)
        .filter((n) => !Number.isNaN(n) && n > 0);
      const top = Math.max(...numbers);
      return `Самый тяжёлый: ${top} т.`;
    }

    const today = payload.filter((l) => l.day === "сегодня");
    const top = today.reduce((a, b) => (b.tons > a.tons ? b : a));
    return `Самый тяжёлый из сегодняшних: ${top.id}, ${top.tons} т.`;
  }
}

export function play(agent: { run: (q: string) => [string, number] }): [string, number] {
  PASSED.length = 0;
  return agent.run(QUESTION);
}

export function verify(result: [string, number]): [boolean, string][] {
  const [answer, steps] = result;
  const payload = PASSED[0];
  const shaped = isRecords(payload);
  const fields = shaped ? ["id", "tons", "day"].filter((f) => f in payload[0]) : [];
  return [
    [shaped, `форма данных: ${shaped ? "записи" : "сплошной текст"}`],
    [fields.length === 3, `полей в записи: ${fields.length} из 3`],
    [
      typeof answer === "string" && answer.includes(HEAVIEST_TODAY),
      `ответ агента: ${answer}`,
    ],
    [steps <= 2, `обращений к модели: ${steps} (допустимо 2)`],
  ];
}
