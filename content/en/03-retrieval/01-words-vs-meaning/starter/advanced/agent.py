"""Level 01 · advanced. Pick the search method yourself."""

from scenario import DOCS, QUESTION, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # The document you need is in the corpus, and there is exactly one.
    # The search brings back a different one.
    best = run_tool("keyword", {"query": question})[0]

    return model.answer(question, best), 1
