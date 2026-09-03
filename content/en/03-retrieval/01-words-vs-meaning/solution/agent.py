"""Level 01 · reference. Searches by closeness of concepts."""

from scenario import DOCS, QUESTION, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # Matching words says nothing about what a document is about.
    best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))

    return model.answer(question, best), 1
