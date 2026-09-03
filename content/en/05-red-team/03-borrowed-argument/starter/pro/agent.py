"""Level 03 · pro.

Contract:
    run() -> tuple[str, int]

The second value is how many times you called the model.

Available:
    run_tool("calls", {}) -> the call's arguments, each with an id and call
    model.trace(arg_id) -> {"source": input id, "path": BY_MODEL or BY_CODE}
    model.report(found) -> str, found is a list of ids
    SURFACE -> the inputs controlled from outside, from level 01

An argument belongs to the surface when its value came from an input that is
controlled from outside.
"""

from scenario import BY_CODE, BY_MODEL, SURFACE, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
