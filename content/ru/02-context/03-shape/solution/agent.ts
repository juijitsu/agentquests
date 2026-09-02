/** Уровень 03 · эталон. Данные уходят записями, а не абзацем. */

import { Model, SENTENCES, parse } from "../scenario.ts";

export function run(question: string): [string, number] {
  const model = new Model();

  // Форма — часть данных: пока вес и день лежат в одной записи,
  // их можно сопоставить. В абзаце они просто рядом.
  const payload = SENTENCES.map(parse);

  return [model.ask(question, payload), 1];
}
