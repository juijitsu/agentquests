"""Level 05 · advanced. Work out why only the warehouse half was found."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # The search worked correctly and returned two fitting documents.
    # Both are about one half of the question.
    found = run_tool("search", {"query": question})

    return model.reply(question, found), 1
