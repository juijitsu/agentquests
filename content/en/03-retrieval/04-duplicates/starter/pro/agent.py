"""Level 04 · pro.

Contract:
    run(question: str) -> tuple[str, int]

Available:
    CHUNKS, TOP_K — the corpus and the selection size
    model.similarity(left, right) -> closeness of two texts
    model.same_fact(left, right) -> whether it is one fact in different words
    model.reply(question, selection) -> str

The question needs two facts. One of them is retold in five documents and
fills the entire selection on its own.
"""

from scenario import CHUNKS, TOP_K, Model


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
