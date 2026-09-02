"""Уровень 05 · эталон. Показания накапливаются вместе с источником."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    facts = run_tool("facts", {})

    # Одно поле — сколько угодно показаний. Схлопывать их здесь значит
    # принять решение, которое принимать не нам.
    merged = {}
    for fact in facts:
        merged.setdefault(fact["field"], []).append((fact["source"], fact["value"]))

    return model.ask(question, merged), 1
