"""Level 07 · reference. The cost is counted alongside the metric."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    metric, harm = {}, {}

    # The metric says what there is more of. The goal says what it cost.
    for version in ("old", "new"):
        answers = {
            c["id"]: run_tool("answer", {"version": version, "case": c["id"]})
            for c in CASES
        }
        metric[version] = round(
            100 * sum(model.is_specific(a) for a in answers.values()) / len(CASES)
        )
        harm[version] = sum(
            model.is_specific(answers[c["id"]])
            and not model.is_correct(c["expected"], answers[c["id"]])
            for c in CASES
        )

    return model.report(metric, harm), 1
