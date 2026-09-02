"""Уровень 08 · продвинутый.

Отчёт обязан удовлетворять пяти условиям сразу:

    судья независимый          — автор засчитывает себе всё
    утечка исключена           — два случая лежат в промпте
    прогонов несколько         — иначе сломанное неотличимо от неустойчивого
    разбивка по видам          — общий процент прячет провал
    устойчивость учтена        — верный через раз не считается верным

Ниже — отчёт, нарушающий все пять.
"""

from scenario import CASES, RUBRIC, RUNS, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    passed = sum(
        model.judge_own(run_tool("answer", {"case": c["id"], "run": 0}))
        for c in CASES
    )
    by_kind = {"всё": round(100 * passed / len(CASES))}
    return model.decide(by_kind, []), 1
