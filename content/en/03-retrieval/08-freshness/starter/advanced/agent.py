"""Level 08 · advanced. Add the second signal yourself."""

from scenario import DOCS, Model


def run(question: str) -> tuple[str, int]:
    model = Model()

    # The document found is about that very lane and holds a rate.
    # The rate has been in force since February of the year before last.
    best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))

    return model.reply(question, best), 1
