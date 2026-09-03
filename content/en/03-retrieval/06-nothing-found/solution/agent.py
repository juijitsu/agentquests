"""Level 06 · reference. Similarity gets a floor, not only an order."""

from scenario import DOCS, THRESHOLD, Model


def run(question: str) -> tuple[str, int]:
    model = Model()
    best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))

    # Order answers "who is best". The threshold answers "is that good enough".
    if model.similarity(question, best["text"]) < THRESHOLD:
        return model.say_missing(question), 1

    return model.reply(question, best), 1
