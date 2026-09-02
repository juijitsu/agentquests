/** Уровень 06 · новичок. Бриф набирается от свежего к старому. */

import { BLOCKS, BUDGET, Model, type Block } from "../../scenario.ts";

export function run(question: string): [string, number] {
  const model = new Model();

  // TODO: возраст блока ничего не говорит о его ценности. Ограничение на
  //       мосту поставили в 2019 году, и оно решает вопрос. Сортируйте по
  //       отдаче на единицу стоимости — model.worth(b) / b.cost, по убыванию.
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
