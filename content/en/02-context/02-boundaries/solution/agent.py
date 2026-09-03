"""Level 02 · reference. Every line goes out with its own source."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    lines = run_tool("about", {"topic": model.topic(question)}).split(" | ")

    # The boundary the selection destroyed is restored right here.
    blocks = [f'{run_tool("source", {"line": line})}: {line}' for line in lines]

    return model.ask(question, blocks), 1
