"""Уровень 06 · эталон. Каждый случай прогоняется несколько раз."""

from scenario import CASES, RUNS, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()

    # Один прогон говорит, что случилось. Несколько — что случается.
    stable_ok, flaky = [], []
    for case in CASES:
        results = [
            run_tool("check", {"case": case["id"], "run": n}) == "верно"
            for n in range(RUNS)
        ]
        if all(results):
            stable_ok.append(case["id"])
        elif any(results):
            flaky.append(case["id"])

    return model.report(stable_ok, flaky, len(CASES)), 1
