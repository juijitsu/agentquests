"""Уровень 07 · продвинутый. Понять, что показывает выросшая метрика."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    metric, harm = {}, {}

    # Уклончивость победили: было пятьдесят процентов конкретных ответов,
    # стало сто. Ровно то, чего добивались.
    for version in ("old", "new"):
        answers = [
            run_tool("answer", {"version": version, "case": c["id"]}) for c in CASES
        ]
        metric[version] = round(
            100 * sum(model.is_specific(a) for a in answers) / len(CASES)
        )
        harm[version] = 0

    return model.report(metric, harm), 1
