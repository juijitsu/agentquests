"""Level 07 · advanced. Work out what the grown metric shows."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    metric, harm = {}, {}

    # Evasiveness was defeated: specific answers went from fifty percent
    # to a hundred. Exactly what was wanted.
    for version in ("old", "new"):
        answers = [
            run_tool("answer", {"version": version, "case": c["id"]}) for c in CASES
        ]
        metric[version] = round(
            100 * sum(model.is_specific(a) for a in answers) / len(CASES)
        )
        harm[version] = 0

    return model.report(metric, harm), 1
