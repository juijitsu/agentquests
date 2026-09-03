"""Level 01 · pro.

Contract:
    run(question: str) -> tuple[str, int]

Available:
    run_tool("about", {"topic": ...}) -> fitting papers joined by " | "
    model.topic(question) -> str      -> what the question is about
    model.ask(question, blocks) -> str -> an answer from the blocks you pass

The model reads no more than six blocks in full; from a long list it sees only
the first three and the last three. The paper that matters sits exactly in the
middle of the folder.
"""

from scenario import DOCS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
