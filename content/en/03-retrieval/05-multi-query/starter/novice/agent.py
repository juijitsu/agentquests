"""Level 05 · novice. One query for a question made of two halves."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # TODO: the question holds two different queries and is searched as one.
    #       Split it: model.split(question) returns the sub-questions — search
    #       for each separately and merge what was found, dropping repeats by id.
    found = run_tool("search", {"query": question})

    return model.reply(question, found), 1
