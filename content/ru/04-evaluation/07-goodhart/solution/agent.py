"""Уровень 07 · эталон. Рядом с метрикой считается вред."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    metric, harm = {}, {}

    # Метрика говорит, чего стало больше. Цель — чего это стоило.
    for version in ("old", "new"):
        answers = {
            c["id"]: run_tool("answer", {"version": version, "case": c["id"]})
            for c in CASES
        }
        metric[version] = round(
            100 * sum(model.is_specific(a) for a in answers.values()) / len(CASES)
        )
        harm[version] = sum(
            model.is_specific(answers[c["id"]])
            and not model.is_correct(c["expected"], answers[c["id"]])
            for c in CASES
        )

    return model.report(metric, harm), 1
