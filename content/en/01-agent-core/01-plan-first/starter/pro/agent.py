"""Level 01 · pro.

Contract:
    run(question: str) -> tuple[str, int]

The task requires walking every leg of the route and returning the end-to-end
time. The model follows a plan only if it sits in the history as its own
message with the role "plan". Without one it sees just the nearest step.

Available: model.make_plan(question) -> list[str]
"""

from scenario import Model, TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
