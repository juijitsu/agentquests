"""Level 05 · pro.

Contract:
    run(question: str) -> tuple[str, int]

The model on this level never finishes. The agent must stop on the tenth
iteration and return a message that makes clear how many steps were spent
and which tool everything got stuck on. An exception escaping is not an
answer.
"""

from scenario import Model, TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
