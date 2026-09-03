"""Level 09 · pro. The finale of the track.

Contract:
    run(question: str) -> tuple[str, int]

Available:
    DOCS, TOP_K, THRESHOLD
    run_tool("exact", {"token": ...}) -> literal occurrences
    model.split(question) -> sub-questions
    model.identifier(part) -> the identifier, if there is one
    model.similarity(left, right), model.freshness(doc), model.same_fact(a, b)
    model.say_missing(part) -> an honest refusal
    model.reply(question, selection) -> str

selection is a list with one element per sub-question: either a selection of
documents or a refusal string.

The answer counts if both halves were handled; the selection holds no other
waybills; the full cost for 4471 is named; and the nonexistent bridge gets a
refusal naming the subject.
"""

from scenario import DOCS, THRESHOLD, TOP_K, Model, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
