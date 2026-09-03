"""Level 06 · reference. Every case is run several times."""

from scenario import CASES, RUNS, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()

    # One run tells you what happened. Several tell you what happens.
    stable_ok, flaky = [], []
    for case in CASES:
        results = [
            run_tool("check", {"case": case["id"], "run": n}) == "correct"
            for n in range(RUNS)
        ]
        if all(results):
            stable_ok.append(case["id"])
        elif any(results):
            flaky.append(case["id"])

    return model.report(stable_ok, flaky, len(CASES)), 1
