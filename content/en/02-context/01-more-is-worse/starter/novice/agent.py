"""Level 01 · novice. The whole haul folder goes into the window."""

from scenario import DOCS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # TODO: the model will not read twenty-two papers in full — from a long
    #       list it sees only the beginning and the end. Ask which of them
    #       bear on the matter: run_tool("about", {"topic": model.topic(question)})
    #       returns them joined by " | ", and only those should go into the window.
    blocks = list(DOCS)

    return model.ask(question, blocks), 1
