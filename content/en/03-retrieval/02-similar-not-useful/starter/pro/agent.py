"""Level 02 · pro.

Contract:
    run(question: str) -> tuple[str, int]

Available:
    DOCS — the corpus
    model.similarity(left, right) -> how much the document is about the same thing
    model.answers(question, doc) -> whether what is sought is inside it
    model.reply(question, doc) -> str

Similarity and fitness are different questions. The most similar document does
not answer this question, and the one that does is only second by similarity.
"""

from scenario import DOCS, Model


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
