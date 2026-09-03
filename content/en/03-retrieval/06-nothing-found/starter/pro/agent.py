"""Level 06 · pro.

Contract:
    run(question: str) -> tuple[str, int]

run() will be called twice: on a question whose answer is not in the corpus,
and on a question whose answer is. Both have to pass.

Available:
    DOCS, THRESHOLD
    model.similarity(left, right) -> closeness, 0 to 1
    model.say_missing(question) -> an honest refusal naming the subject
    model.reply(question, doc) -> an answer from a document

Ranking always gives you a first. It does not say whether that one is good
enough.
"""

from scenario import DOCS, THRESHOLD, Model


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
