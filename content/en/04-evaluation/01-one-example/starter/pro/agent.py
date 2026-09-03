"""Level 01 · pro.

Contract:
    run() -> tuple[str, int]

There is no argument: what gets measured is not the answer to a question but
the behaviour of the system.

Available:
    CASES — the set of cases; each has id, question and expected
    run_tool("ask", {"version": "old"|"new", "case": id}) -> that version's answer
    model.verdict(old_passed, new_passed, total) -> str

The fix was made for one case, and on that one it works.
"""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
