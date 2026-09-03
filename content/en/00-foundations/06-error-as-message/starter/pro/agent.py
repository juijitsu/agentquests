"""Level 06 · pro.

Contract:
    run(question: str) -> tuple[str, int]

The request has a typo in the crossing name. run_tool will raise ValueError,
and its text lists the allowed values. The agent must reach the right answer
in three iterations, without crashing and without giving up.
"""

from scenario import Model, TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
