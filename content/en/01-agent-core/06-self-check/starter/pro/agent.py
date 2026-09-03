"""Level 06 · pro.

Contract:
    run(question: str) -> tuple[str, int]

Available:
    model.review(answer, question) -> str

Every tool will run without errors. The contradiction appears in the
assembled result. The model is the one to check the terms against the
total: if the comparison ends up in your code, it is not an agent
self-check.
"""

from scenario import Model, TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
