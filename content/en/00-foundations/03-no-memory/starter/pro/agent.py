"""Level 03 · pro.

Contract:
    run(question: str) -> tuple[str, int]   # agent answer, iterations spent

The model will check four legs of the route and then price the haul from the
load weight. The weight is named once — in the original question.
"""

from scenario import Model, TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
