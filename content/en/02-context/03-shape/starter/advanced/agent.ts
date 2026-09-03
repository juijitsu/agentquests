/** Level 03 · advanced. Pick the shape yourself. */

import { Model, SENTENCES, parse } from "../../scenario.ts";

export function run(question: string): [string, number] {
  const model = new Model();

  // All five loads were passed, nothing lost and nothing shortened.
  // The answer is still about the wrong loads.
  const payload = SENTENCES.join(" ");

  return [model.ask(question, payload), 1];
}
