"""Level 07 · pro.

Contract:
    run(question: str) -> tuple[str, int]

Available:
    DOCS
    run_tool("exact", {"token": ...}) -> documents with a literal occurrence
    model.identifier(question) -> the identifier from the question, if any
    model.similarity(left, right) -> closeness by meaning
    model.reply(question, doc) -> str

Neither of the two search methods will do on its own here: meaning does not
tell numbers apart, and exact matching catches on punctuation.
"""

from scenario import DOCS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
