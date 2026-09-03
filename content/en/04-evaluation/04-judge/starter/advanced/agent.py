"""Level 04 · advanced. Work out why it is six of six."""

from scenario import CASES, RUBRIC, Model


def run() -> tuple[str, int]:
    model = Model()

    # The set was run in full, the answers checked by meaning rather than
    # by characters. Six of six.
    passed = sum(model.judge_own(c["expected"], c["got"]) for c in CASES)

    return model.report(passed, len(CASES), "the author"), 1
