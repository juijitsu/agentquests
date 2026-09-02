/** Шестая смена трека. Всё относится к делу, и всё равно не влезает. */

export const TITLE = "Трек «Контекст» · Уровень 06 · Бюджет контекста";
export const BRIEF = `Пять блоков по делу, бюджета хватает на три.
Решающее ограничение — самое старое, и его выбрасывают первым.`;

export type Block = { id: string; text: string; cost: number; dated: string };

export const BUDGET = 80;
export const DECISIVE = ["bridge-limit", "cargo-weight"];

const TONS = 24;
const BRIDGE = 18;

export const BLOCKS: Block[] = [
  { id: "bridge-limit", text: "мост Кэрролл на I-55: ограничение 18 т", cost: 20, dated: "2019-04-11" },
  { id: "bridge-history", text: "история ремонтов моста Кэрролл, 2019–2024", cost: 70, dated: "2025-11-30" },
  { id: "weather", text: "погода по маршруту на сутки вперёд", cost: 25, dated: "2026-09-02" },
  { id: "cargo-weight", text: "вес груза TX-118 по весовой: 24 т", cost: 20, dated: "2026-09-02" },
  { id: "driver-log", text: "отметки водителя за смену", cost: 25, dated: "2026-09-02" },
];

/** Ценность блока для этого вопроса. Судит модель, а не ваш код. */
const WORTH: Record<string, number> = {
  "bridge-limit": 9,
  "bridge-history": 10,
  "weather": 3,
  "cargo-weight": 9,
  "driver-log": 2,
};

export const PASSED: Block[] = [];

export class Model {
  worth(block: Block): number {
    return WORTH[block.id] ?? 0;
  }

  ask(question: string, brief: Block[]): string {
    PASSED.length = 0;
    PASSED.push(...brief);

    const ids = new Set(brief.map((b) => b.id));
    const missing = DECISIVE.filter((id) => !ids.has(id));
    if (missing.length > 0) {
      return "В брифе не хватает данных, чтобы решить: ограничений не нашёл.";
    }
    const verdict = TONS <= BRIDGE ? "пройдёт" : "не пройдёт";
    return `Груз ${TONS} т, мост держит ${BRIDGE} т — ${verdict}.`;
  }
}

export function play(agent: { run: (q: string) => [string, number] }): [string, number] {
  PASSED.length = 0;
  return agent.run("Пройдёт ли TX-118 по мосту Кэрролл?");
}

export function verify(result: [string, number]): [boolean, string][] {
  const [answer, steps] = result;
  const spent = PASSED.reduce((sum, b) => sum + b.cost, 0);
  const ids = new Set(PASSED.map((b) => b.id));
  const present = DECISIVE.filter((id) => ids.has(id));
  const listing = DECISIVE.map((id) => `${id} — ${ids.has(id) ? "да" : "нет"}`).join(", ");
  return [
    [spent <= BUDGET, `потрачено бюджета: ${spent} из ${BUDGET}`],
    [present.length === DECISIVE.length, `решающие блоки: ${listing}`],
    [
      typeof answer === "string" && answer.includes("не пройдёт"),
      `ответ агента: ${answer}`,
    ],
    [steps <= 2, `обращений к модели: ${steps} (допустимо 2)`],
  ];
}
