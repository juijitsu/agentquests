"""Level 02 · advanced. Add the second criterion yourself."""

from scenario import DOCS, Model


def run(question: str) -> tuple[str, int]:
    model = Model()

    # The search worked correctly: the document found really is about this rate
    # and this lane. The answer is not in it.
    best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))

    return model.reply(question, best), 1
