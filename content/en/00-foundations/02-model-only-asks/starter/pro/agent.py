"""Level 02 · pro.

Contract:
    run(question: str) -> tuple[str, int]   # agent answer, iterations spent

On this level the model returns text and tool_calls at the same time.
The notification has to actually go out, not merely be promised.
"""

from scenario import Model, TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
