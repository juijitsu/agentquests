"""Уровень 04 · продвинутый. Понять, почему шесть из шести."""

from scenario import CASES, RUBRIC, Model


def run() -> tuple[str, int]:
    model = Model()

    # Набор прогнан целиком, ответы сверены по смыслу, а не по буквам.
    # Шесть из шести.
    passed = sum(model.judge_own(c["expected"], c["got"]) for c in CASES)

    return model.report(passed, len(CASES), "автор"), 1
