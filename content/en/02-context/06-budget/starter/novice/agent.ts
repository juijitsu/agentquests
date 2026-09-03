/** Level 06 · novice. The brief is built from fresh to old. */

import { BLOCKS, BUDGET, Model, type Block } from "../../scenario.ts";

export function run(question: string): [string, number] {
  const model = new Model();

  // TODO: a block's age says nothing about its value. The bridge limit was set
  //       in 2019, and it is what settles the question. Sort by return per unit
  //       of cost — model.worth(b) / b.cost, descending.
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
