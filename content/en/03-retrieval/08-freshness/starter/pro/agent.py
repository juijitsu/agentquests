"""Level 08 · pro.

Contract:
    run(question: str) -> tuple[str, int]

Available:
    DOCS — every document has a dated field
    model.similarity(left, right) -> closeness by meaning
    model.freshness(doc) -> by how much the document has been discounted
    model.reply(question, doc) -> str

The most similar document here is from last year, and the freshest is about a
different lane. Neither signal on its own gives the right answer.
"""

from scenario import DOCS, Model


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
