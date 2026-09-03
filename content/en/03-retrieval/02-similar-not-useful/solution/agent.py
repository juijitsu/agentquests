"""Level 02 · reference. Fit ones first, then the most similar among them."""

from scenario import DOCS, Model


def run(question: str) -> tuple[str, int]:
    model = Model()

    # Two steps, and the order matters: fitness narrows the field,
    # similarity picks the best of what is left.
    fit = [d for d in DOCS if model.answers(question, d)]
    best = max(fit, key=lambda d: model.similarity(question, d["text"]))

    return model.reply(question, best), 1
