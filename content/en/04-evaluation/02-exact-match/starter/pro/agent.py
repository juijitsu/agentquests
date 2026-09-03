"""Level 02 · pro.

Contract:
    run() -> tuple[str, int]

Available:
    CASES — the set of cases
    run_tool("ask", {"version": ..., "case": ...}) -> that version's answer
    model.same_answer(expected, got) -> the same answer or a different one
    model.verdict(old_passed, new_passed, total) -> str

The new version answers every case correctly. Some of the answers are phrased
differently from the set.
"""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
