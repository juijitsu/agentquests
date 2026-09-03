"""Level 05 · pro.

Contract:
    run(question: str) -> tuple[str, int]

Available:
    model.make_plan(question, blocked=None) -> list[str]

One of the hops will turn out to be closed. The model invents the way around —
but only if you ask it to. The name of the detour must not appear anywhere in
your code: that turns the agent into a script.
"""

from scenario import Model, TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
