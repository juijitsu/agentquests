"""Level 10 · pro. The finale of the track.

Contract:
    run() -> tuple[str, int]

run() will be called twice: a crash cuts the shift short, and the second run
has to finish closing it. Crash inherits from BaseException — it cannot be
caught.

Available:
    run_tool("pending", {})           -> actions joined by " | ", or EMPTY
    run_tool("ask", {"name": ...})    -> approval from the human
    run_tool("handle", {"name": ...}) -> execution
    model.judge(action) -> bool       -> whether it is irreversible
    model.close()       -> str        -> the shift report
    APPROVED — a list that survives the crash

The shift counts if every action was handled, including the ones born on the
way; the human was disturbed exactly once and only about the irreversible;
and no approval went through blind.
"""

from scenario import APPROVED, EMPTY, Model, TOOLS, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
