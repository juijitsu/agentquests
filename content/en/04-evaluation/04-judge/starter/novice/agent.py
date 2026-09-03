"""Level 04 · novice. The author grades itself."""

from scenario import CASES, RUBRIC, Model


def run() -> tuple[str, int]:
    model = Model()

    # TODO: the author knows what it meant to say and scores its own evasion
    #       as precision. Judging belongs to whoever sees only the expected and
    #       received answer: model.judge_blind(RUBRIC, c["expected"], c["got"]).
    passed = sum(model.judge_own(c["expected"], c["got"]) for c in CASES)

    return model.report(passed, len(CASES), "the author"), 1
