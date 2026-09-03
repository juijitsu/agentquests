/** Level 06 · pro.
 *
 * Contract:
 *     run(question: string): [string, number]
 *
 * Available:
 *     BLOCKS: Block[]        — { id, text, cost, dated }, all relevant
 *     BUDGET: number         — how much cost fits
 *     model.worth(block)     — the block's value for this question
 *
 * The budget does not cover everything. Selecting by age will not do: the
 * decisive limit is the oldest. Selecting by value alone will not do either:
 * the most valuable block and the most expensive one are the same, and it
 * crowds out the two cheap blocks that settle the question.
 */

import { BLOCKS, BUDGET, Model, type Block } from "../../scenario.ts";

export function run(question: string): [string, number] {
  const error = new Error("not implemented");
  error.name = "NotImplemented";
  throw error;
}
