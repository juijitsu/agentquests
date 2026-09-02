/** Уровень 06 · эталон. Отбор по отдаче на единицу стоимости. */

import { BLOCKS, BUDGET, Model, type Block } from "../scenario.ts";

export function run(question: string): [string, number] {
  const model = new Model();

  // Не «что ценнее» и не «что свежее», а «что даёт больше на потраченное».
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
