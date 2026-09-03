/** Level 06 · advanced. Choose the selection order yourself. */

import { BLOCKS, BUDGET, Model, type Block } from "../../scenario.ts";

export function run(question: string): [string, number] {
  const model = new Model();

  // All five blocks bear on the question. The budget does not cover all of them.
  const ranked = [...BLOCKS].sort((a, b) => b.dated.localeCompare(a.dated));

  const brief: Block[] = [];
  let spent = 0;
  for (const block of ranked) {
    if (spent + block.cost <= BUDGET) {
      brief.push(block);
      spent += block.cost;
    }
  }

  return [model.ask(question, brief), 1];
}
