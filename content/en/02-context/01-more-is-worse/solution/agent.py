"""Level 01 · reference. What goes into the window is selected, not everything."""

from scenario import DOCS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # Not "what do we have" but "what bears on the question".
    blocks = run_tool("about", {"topic": model.topic(question)}).split(" | ")

    return model.ask(question, blocks), 1
