"""Уровень 07 · новичок. Меряет только то, что улучшали."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    metric, harm = {}, {}

    # TODO: конкретность — не цель, а признак, которым цель заменили.
    #       Посчитайте вторым числом вред: ответ конкретный и при этом
    #       неверный. Верность спрашивайте у model.is_correct.
    for version in ("old", "new"):
        answers = [
            run_tool("answer", {"version": version, "case": c["id"]}) for c in CASES
        ]
        metric[version] = round(
            100 * sum(model.is_specific(a) for a in answers) / len(CASES)
        )
        harm[version] = 0

    return model.report(metric, harm), 1
