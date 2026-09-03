"""Level 06 · advanced. Work out what the ranking is missing."""

from scenario import DOCS, THRESHOLD, Model


def run(question: str) -> tuple[str, int]:
    model = Model()
    best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))

    # The search worked correctly and returned the most similar document.
    # It is the most similar one and it is still the wrong one.
    return model.reply(question, best), 1
