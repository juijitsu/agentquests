"""Level 04 · pro.

Contract:
    TOOLS — a list of two tools: check_border_status(crossing)
            and estimate_cost(weight_tons)
    run(question: str) -> tuple[str, int]

The agent must pick check_border_status for a question about waiting at a
crossing, without the tool name appearing in the question itself.
"""

from scenario import Model, run_tool

TOOLS = []


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
