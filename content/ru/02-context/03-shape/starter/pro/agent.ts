/** Уровень 03 · профессионал.
 *
 * Контракт:
 *     run(question: string): [string, number]
 *
 * Доступно:
 *     SENTENCES: string[]              — как данные приходят из диспетчерской
 *     parse(sentence): Load            — разбирает одно предложение в запись
 *     model.ask(question, payload)     — payload любой формы
 *
 * Вопрос требует отобрать по дню и сравнить по весу. Сплошной текст
 * позволяет достать числа, но не связать их с полями.
 */

import { Model, SENTENCES, parse } from "../../scenario.ts";

export function run(question: string): [string, number] {
  const error = new Error("не реализовано");
  error.name = "NotImplemented";
  throw error;
}
