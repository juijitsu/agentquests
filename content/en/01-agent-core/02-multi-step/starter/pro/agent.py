"""Level 02 · pro.

Contract:
    run(question: str) -> tuple[str, int]

The route is not known up front. The tool next_hop(city) returns one next
stop. After every hop the model reports in text and stops asking for tools —
but the task is solved only once Newark is reached. The stopping condition
is yours.
"""

from scenario import Model, TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
