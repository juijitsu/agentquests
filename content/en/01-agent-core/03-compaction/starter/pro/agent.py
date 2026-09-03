"""Level 03 · pro.

Contract:
    run(question: str) -> tuple[str, int]

The model accepts at most 8 messages per call and raises ValueError beyond
that. A six-hop route does not fit. The rate is named once — in the original
task — and is needed at the very end.
"""

from scenario import Model, TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
