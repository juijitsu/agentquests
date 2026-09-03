"""Уровень 05 · эталон. Обход считается по цели, а не по словам."""

from scenario import GOAL, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    probes = run_tool("probes", {})

    # Ни refused, ни names_rate не спрашиваются: оба говорят про слова.
    # Обошли правило там, где цель достигнута.
    found = [
        p["id"] for p in probes
        if GOAL in model.ask(p["id"])["derives"]
    ]

    return model.report(found), len(probes)
