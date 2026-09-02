/** Уровень 03 · новичок. Записи склеены обратно в текст. */

import { Model, SENTENCES, parse } from "../../scenario.ts";

export function run(question: string): [string, number] {
  const model = new Model();

  // TODO: склейка предложений возвращает данные в ту самую форму, из-за
  //       которой теряется условие «сегодня». Разберите каждое предложение
  //       через parse и передайте массив записей, а не строку.
  const payload = SENTENCES.join(" ");

  return [model.ask(question, payload), 1];
}
