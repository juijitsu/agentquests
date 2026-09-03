/** Sixth shift of the track. Everything is relevant, and it still does not fit. */

export const LANG = "en";
export const TITLE = "Context track · Level 06 · The context budget";
export const BRIEF = `Five relevant blocks, a budget that covers three.
The decisive limit is the oldest one, and it gets thrown out first.`;

export type Block = { id: string; text: string; cost: number; dated: string };

export const BUDGET = 80;
export const DECISIVE = ["bridge-limit", "cargo-weight"];

const TONS = 24;
const BRIDGE = 18;

export const BLOCKS: Block[] = [
  { id: "bridge-limit", text: "Carroll bridge on I-55: limit 18 t", cost: 20, dated: "2019-04-11" },
  { id: "bridge-history", text: "Carroll bridge repair history, 2019–2024", cost: 70, dated: "2025-11-30" },
  { id: "weather", text: "weather along the route for the next day", cost: 25, dated: "2026-09-02" },
  { id: "cargo-weight", text: "weight of load TX-118 per the weigh ticket: 24 t", cost: 20, dated: "2026-09-02" },
  { id: "driver-log", text: "driver's marks for the shift", cost: 25, dated: "2026-09-02" },
];

/** A block's value for this question. The model judges it, not your code. */
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
      return "The brief is missing data to decide: found no limits.";
    }
    const verdict = TONS <= BRIDGE ? "will pass" : "will not pass";
    return `Load ${TONS} t, the bridge holds ${BRIDGE} t — ${verdict}.`;
  }
}

export function play(agent: { run: (q: string) => [string, number] }): [string, number] {
  PASSED.length = 0;
  return agent.run("Will TX-118 pass over the Carroll bridge?");
}

export function verify(result: [string, number]): [boolean, string][] {
  const [answer, steps] = result;
  const spent = PASSED.reduce((sum, b) => sum + b.cost, 0);
  const ids = new Set(PASSED.map((b) => b.id));
  const present = DECISIVE.filter((id) => ids.has(id));
  const listing = DECISIVE.map((id) => `${id} — ${ids.has(id) ? "yes" : "no"}`).join(", ");
  return [
    [spent <= BUDGET, `budget spent: ${spent} of ${BUDGET}`],
    [present.length === DECISIVE.length, `decisive blocks: ${listing}`],
    [
      typeof answer === "string" && answer.includes("will not pass"),
      `agent answer: ${answer}`,
    ],
    [steps <= 2, `calls to the model: ${steps} (2 allowed)`],
  ];
}
