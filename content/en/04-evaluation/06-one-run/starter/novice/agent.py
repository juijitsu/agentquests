"""Level 06 · novice. Measures from a single run."""

from scenario import CASES, RUNS, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()

    # TODO: two cases answer every other time, and on run zero both came out
    #       lucky. Run every case RUNS times, separate the stably correct from
    #       the unstable ones and pass both lists to report.
    passed = [
        c["id"] for c in CASES
        if run_tool("check", {"case": c["id"], "run": 0}) == "correct"
    ]

    return model.report(passed, [], len(CASES)), 1
