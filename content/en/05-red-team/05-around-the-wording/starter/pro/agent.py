"""Level 05 · pro.

Contract:
    run() -> tuple[str, int]

The second value is how many times you called the model.

Available:
    run_tool("probes", {}) -> the probes in the set, each with an id and text
    model.ask(probe_id) -> {"refused": bool, "names_rate": bool, "derives": list}
    model.report(found) -> str, found is a list of ids
    RULE -> the rule as it is written
    GOAL -> what the rule exists for

A probe got around the rule if the answer yields GOAL, whatever words it was
written in.
"""

from scenario import GOAL, RULE, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
