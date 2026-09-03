/** Level 06 · reference. Selection by return per unit of cost. */

import { BLOCKS, BUDGET, Model, type Block } from "../scenario.ts";

export function run(question: string): [string, number] {
  const model = new Model();

  // Not "which is more valuable" and not "which is fresher", but
  // "which gives more per unit spent".
  const ranked = [...BLOCKS].sort(
    (a, b) => model.worth(b) / b.cost - model.worth(a) / a.cost,
  );

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
