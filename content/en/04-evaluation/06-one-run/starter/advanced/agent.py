"""Level 06 · advanced. Work out what one run gives you."""

from scenario import CASES, RUNS, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()

    # Five of six. The set is clean, the judge independent, no leak.
    passed = [
        c["id"] for c in CASES
        if run_tool("check", {"case": c["id"], "run": 0}) == "correct"
    ]

    return model.report(passed, [], len(CASES)), 1
