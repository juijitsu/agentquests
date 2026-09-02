"""Уровень 04 · новичок. Автор оценивает сам себя."""

from scenario import CASES, RUBRIC, Model


def run() -> tuple[str, int]:
    model = Model()

    # TODO: автор знает, что хотел сказать, и засчитывает себе уклончивое
    #       как точное. Судить должен тот, кто видит только эталон и ответ:
    #       model.judge_blind(RUBRIC, c["expected"], c["got"]).
    passed = sum(model.judge_own(c["expected"], c["got"]) for c in CASES)

    return model.report(passed, len(CASES), "автор"), 1
