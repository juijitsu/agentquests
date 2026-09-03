"""Level 02 · advanced. Restore the boundary yourself."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    lines = run_tool("about", {"topic": model.topic(question)}).split(" | ")

    # Exactly what was needed got selected. Three lines about reefers —
    # and the answer is still about somebody else's surcharge.
    blocks = lines

    return model.ask(question, blocks), 1
