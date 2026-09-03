"""Level 01 · pro.

Contract:
    run(question: str) -> tuple[str, int]

Available:
    DOCS — the corpus; every document has id, text and concepts
    run_tool("keyword", {"query": ...}) -> documents by word match
    model.embed(text) -> a set of concepts
    model.similarity(left, right) -> share of shared concepts, 0 to 1
    model.answer(question, doc) -> str

The question and the document you need describe the same thing in different
words.
"""

from scenario import DOCS, QUESTION, Model, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
