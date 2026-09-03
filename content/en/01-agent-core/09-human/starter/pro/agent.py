"""Level 09 · pro.

Contract:
    run() -> tuple[str, int]

Available:
    run_tool("act", {"name": ...})  -> carries out an action
    run_tool("ask", {"name": ...})  -> sends for approval, returns a verdict
    REFUSED — the list of rejected actions; the model reads it

The model puts an irreversible field into the call arguments. The approver is
a live person on shift, and their attention runs out sooner than your
questions do. A refusal has to stop the action, or approval is meaningless.
"""

from scenario import REFUSED, Model, TOOLS, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
