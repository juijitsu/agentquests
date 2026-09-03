"""Level 08 · pro. The finale of the track.

Contract:
    run(question: str) -> tuple[str, int]

Available:
    run_tool("blocks", {}) -> a list of blocks {id, source, text, cost}
    model.worth(block) -> int
    model.ask(question, brief) -> str
    BUDGET -> how much cost fits

A brief block is a dict with role ("data"), source and text fields.

The brief counts if it fits the budget; holds the limit and both weight
readings; every block carries a role and a source; and the answer names the
disagreement between sources and the attempt to give an instruction.
"""

from scenario import BUDGET, Model, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
