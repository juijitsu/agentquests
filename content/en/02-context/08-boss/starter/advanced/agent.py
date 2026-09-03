"""Level 08 · advanced.

The brief has to satisfy five conditions at once:

    fit the budget                — blocks worth 190, room for 100
    take the decisive             — by return, not by order and not by price
    convey the source dispute     — the weight readings disagree
    mark role and source          — or a paper becomes an instruction
    report the attempted order    — rather than dropping it

Below is an assembler that breaks all five.
"""

from scenario import BUDGET, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    blocks = run_tool("blocks", {})

    brief = []
    spent = 0
    for block in blocks:
        if spent + block["cost"] <= BUDGET:
            brief.append(block["text"])
            spent += block["cost"]

    return model.ask(question, "\n".join(brief)), 1
