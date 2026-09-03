"""Level 02 · pro.

Contract:
    run(question: str) -> tuple[str, int]

Available:
    run_tool("about", {"topic": ...})  -> lines on the topic joined by " | "
    run_tool("source", {"line": ...})  -> whose rate sheet it is
    model.topic(question) -> str
    model.ask(question, blocks) -> str

Selecting by topic pulls lines out of different rate sheets and stacks them
into one list. The model attaches a fact to a signature; where there is no
signature, it attaches it to the first line.
"""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
