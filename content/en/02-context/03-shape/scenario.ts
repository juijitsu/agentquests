/** Third shift of the track. Same facts, different shape — different answer. */

export const LANG = "en";
export const TITLE = "Context track · Level 03 · The shape of data";
export const BRIEF = `Five loads described in sentences, everything labelled and present.
The answer comes back about the heaviest overall, and the question was about today's.`;

export type Load = { id: string; tons: number; day: string };

const LOADS: Load[] = [
  { id: "TX-118", tons: 24, day: "today" },
  { id: "TX-204", tons: 31, day: "tomorrow" },
  { id: "TX-337", tons: 27, day: "today" },
  { id: "TX-441", tons: 19, day: "today" },
  { id: "TX-509", tons: 22, day: "tomorrow" },
];

/** This is how the data arrives from dispatch: as running text. */
export const SENTENCES: string[] = LOADS.map(
  (l) => `Load ${l.id} weighs ${l.tons} t and leaves ${l.day}.`,
);

export const QUESTION = "Which is the heaviest load of the ones leaving today?";
export const HEAVIEST_TODAY = "TX-337";

/** Parses one sentence into a record. String work, not shape work. */
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
      // Numbers can be pulled out of running text, but fields cannot: there is
      // nothing to tie a weight to a departure day, so "today" is lost.
      const numbers = String(payload)
        .split(" ")
        .map(Number)
        .filter((n) => !Number.isNaN(n) && n > 0);
      const top = Math.max(...numbers);
      return `The heaviest: ${top} t.`;
    }

    const today = payload.filter((l) => l.day === "today");
    const top = today.reduce((a, b) => (b.tons > a.tons ? b : a));
    return `Heaviest leaving today: ${top.id}, ${top.tons} t.`;
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
    [shaped, `data shape: ${shaped ? "records" : "running text"}`],
    [fields.length === 3, `fields per record: ${fields.length} of 3`],
    [
      typeof answer === "string" && answer.includes(HEAVIEST_TODAY),
      `agent answer: ${answer}`,
    ],
    [steps <= 2, `calls to the model: ${steps} (2 allowed)`],
  ];
}
