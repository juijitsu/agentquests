"""Level 04 · reference. The one who did not write the answer judges it."""

from scenario import CASES, RUBRIC, Model


def run() -> tuple[str, int]:
    model = Model()

    # The judge is given a rule and two texts. Who wrote them is neither its
    # business nor its problem.
    passed = sum(
        model.judge_blind(RUBRIC, c["expected"], c["got"]) for c in CASES
    )

    return model.report(passed, len(CASES), "independent"), 1
