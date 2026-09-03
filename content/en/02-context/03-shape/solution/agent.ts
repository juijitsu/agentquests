/** Level 03 · reference. The data goes out as records, not as a paragraph. */

import { Model, SENTENCES, parse } from "../scenario.ts";

export function run(question: string): [string, number] {
  const model = new Model();

  // Shape is part of the data: while the weight and the day sit in one
  // record, they can be matched. In a paragraph they are merely adjacent.
  const payload = SENTENCES.map(parse);

  return [model.ask(question, payload), 1];
}
