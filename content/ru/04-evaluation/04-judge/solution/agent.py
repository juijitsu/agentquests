"""Уровень 04 · эталон. Судит тот, кто не писал ответ."""

from scenario import CASES, RUBRIC, Model


def run() -> tuple[str, int]:
    model = Model()

    # Судье дают правило и два текста. Кто автор — не его дело и не его беда.
    passed = sum(
        model.judge_blind(RUBRIC, c["expected"], c["got"]) for c in CASES
    )

    return model.report(passed, len(CASES), "независимый"), 1
