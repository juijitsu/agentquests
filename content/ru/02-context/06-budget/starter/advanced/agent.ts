/** Уровень 06 · продвинутый. Порядок отбора выбрать самому. */

import { BLOCKS, BUDGET, Model, type Block } from "../../scenario.ts";

export function run(question: string): [string, number] {
  const model = new Model();

  // Все пять блоков относятся к вопросу. Бюджета хватает не на все.
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
