"""Level 10 · advanced.

The shift has to close with four conditions holding at once:

    the queue grows as you work   — a snapshot goes stale
    the human is bothered wisely  — their attention runs out
    approval survives a crash     — the process dies halfway
    the loop is finite            — the exit condition is outside

Below is a working dispatcher that breaks the first three. The fourth it
satisfies by accident: walking a snapshot is finite on its own. Live reading
takes that property away.
"""

from scenario import APPROVED, EMPTY, Model, TOOLS, run_tool

MAX_STEPS = 12


def run() -> tuple[str, int]:
    model = Model()
    step = 0

    for action in run_tool("pending", {}).split(" | "):
        step += 1
        run_tool("ask", {"name": action})
        run_tool("handle", {"name": action})

    return model.close(), step
