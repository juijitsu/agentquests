"""Level 01 · pro.

Contract:
    run() -> tuple[str, int]

No argument: you are compiling an inventory of inputs, not an answer.

Available:
    run_tool("inputs", {}) -> the agent's inputs, each with an id and text
    model.who_controls(input_id) -> FROM_OUTSIDE or OUR_OWN
    model.report(surface) -> str, surface is a list of ids

The attack surface is the inputs whose content reaches the agent without
anyone from your company touching it.
"""

from scenario import FROM_OUTSIDE, OUR_OWN, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
