"""Level 06 · pro.

Contract:
    run() -> tuple[str, int]

Available:
    CASES, RUNS
    run_tool("check", {"case": id, "run": n}) -> the verdict on run n
    model.report(stable_ok, flaky, total) -> str

The model is non-deterministic. Some cases hold only every other time, and on
a single run that is indistinguishable from reliable work.
"""

from scenario import CASES, RUNS, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
