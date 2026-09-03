/** Level 03 · pro.
 *
 * Contract:
 *     run(question: string): [string, number]
 *
 * Available:
 *     SENTENCES: string[]              — how the data arrives from dispatch
 *     parse(sentence): Load            — parses one sentence into a record
 *     model.ask(question, payload)     — payload of any shape
 *
 * The question requires filtering by day and comparing by weight. Running
 * text lets you pull out numbers but not tie them to fields.
 */

import { Model, SENTENCES, parse } from "../../scenario.ts";

export function run(question: string): [string, number] {
  const error = new Error("not implemented");
  error.name = "NotImplemented";
  throw error;
}
