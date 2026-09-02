/** Уровень 03 · продвинутый. Форму выбрать самому. */

import { Model, SENTENCES, parse } from "../../scenario.ts";

export function run(question: string): [string, number] {
  const model = new Model();

  // Все пять грузов переданы, ничего не потеряно и не сокращено.
  // Ответ всё равно не про те грузы.
  const payload = SENTENCES.join(" ");

  return [model.ask(question, payload), 1];
}
