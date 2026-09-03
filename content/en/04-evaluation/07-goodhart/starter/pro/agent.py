"""Level 07 · pro.

Contract:
    run() -> tuple[str, int]

Available:
    CASES — every case has expected, sometimes it is "no data"
    run_tool("answer", {"version": ..., "case": ...}) -> that version's answer
    model.is_specific(answer) -> the metric: is the answer specific
    model.is_correct(expected, answer) -> the goal: is the answer right
    model.report(metric, harm) -> str, both arguments {"old": ..., "new": ...}

The metric was introduced to defeat evasiveness. The new version defeated it
completely.
"""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
