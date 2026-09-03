"""Level 08 · advanced.

The report has to satisfy five conditions at once:

    an independent judge     — the author scores everything for itself
    the leak excluded        — two cases sit in the prompt
    several runs             — or broken is indistinguishable from unstable
    a breakdown by kind      — an overall percentage hides the failure
    stability accounted for  — correct-every-other-time is not correct

Below is a report that breaks all five.
"""

from scenario import CASES, RUBRIC, RUNS, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    passed = sum(
        model.judge_own(run_tool("answer", {"case": c["id"], "run": 0}))
        for c in CASES
    )
    by_kind = {"everything": round(100 * passed / len(CASES))}
    return model.decide(by_kind, []), 1
