"""Level 01 · advanced. The selection is left to you."""

from scenario import DOCS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # The bridge limit is in this folder. The answer is wrong anyway.
    blocks = list(DOCS)

    return model.ask(question, blocks), 1
