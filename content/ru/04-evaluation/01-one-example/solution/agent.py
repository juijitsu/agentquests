"""Уровень 01 · эталон. Измеряется набор, а не любимый пример."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()

    # Обе версии проходят один и тот же набор целиком — иначе сравнивать нечего.
    scores = {}
    for version in ("old", "new"):
        scores[version] = sum(
            run_tool("ask", {"version": version, "case": c["id"]}) == c["expected"]
            for c in CASES
        )

    return model.verdict(scores["old"], scores["new"], len(CASES)), 1
