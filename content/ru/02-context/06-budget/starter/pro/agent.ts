/** Уровень 06 · профессионал.
 *
 * Контракт:
 *     run(question: string): [string, number]
 *
 * Доступно:
 *     BLOCKS: Block[]        — { id, text, cost, dated }, все по делу
 *     BUDGET: number         — сколько стоимости помещается
 *     model.worth(block)     — ценность блока для этого вопроса
 *
 * Бюджета хватает не на всё. Отбирать по возрасту нельзя: решающее
 * ограничение самое старое. Отбирать по одной лишь ценности тоже нельзя:
 * самый ценный блок и самый дорогой — один и тот же, и он вытеснит два
 * дешёвых, которые вопрос и решают.
 */

import { BLOCKS, BUDGET, Model, type Block } from "../../scenario.ts";

export function run(question: string): [string, number] {
  const error = new Error("не реализовано");
  error.name = "NotImplemented";
  throw error;
}
