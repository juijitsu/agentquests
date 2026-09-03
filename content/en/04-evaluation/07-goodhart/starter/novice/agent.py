"""Level 07 · novice. Measures only what was being improved."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    metric, harm = {}, {}

    # TODO: specificity is not the goal but the proxy the goal was swapped for.
    #       Count the harm as a second number: an answer that is specific and
    #       wrong at the same time. Ask model.is_correct for correctness.
    for version in ("old", "new"):
        answers = [
            run_tool("answer", {"version": version, "case": c["id"]}) for c in CASES
        ]
        metric[version] = round(
            100 * sum(model.is_specific(a) for a in answers) / len(CASES)
        )
        harm[version] = 0

    return model.report(metric, harm), 1
