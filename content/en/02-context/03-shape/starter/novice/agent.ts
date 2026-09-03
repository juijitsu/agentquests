/** Level 03 · novice. The records are glued back into text. */

import { Model, SENTENCES, parse } from "../../scenario.ts";

export function run(question: string): [string, number] {
  const model = new Model();

  // TODO: joining the sentences returns the data to the very shape that loses
  //       the "today" condition. Parse each sentence with parse and pass an
  //       array of records instead of a string.
  const payload = SENTENCES.join(" ");

  return [model.ask(question, payload), 1];
}
