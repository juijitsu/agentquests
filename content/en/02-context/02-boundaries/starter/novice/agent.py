"""Level 02 · novice. The lines are selected correctly and stripped of names."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    lines = run_tool("about", {"topic": model.topic(question)}).split(" | ")

    # TODO: the selection pulled the lines out of the rate sheets and left them
    #       unsigned — there is no telling whose surcharge is whose. Ask for the
    #       source of every line via run_tool("source", {"line": line}) and glue
    #       the signature to the line: f"{who}: {line}".
    blocks = lines

    return model.ask(question, blocks), 1
