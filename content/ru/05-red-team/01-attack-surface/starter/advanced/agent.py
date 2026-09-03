"""Уровень 01 · продвинутый. Поверхность составить самому."""

from scenario import FROM_OUTSIDE, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    inputs = run_tool("inputs", {})

    # Поле ввода проверено вдоль и поперёк, инъекций там нет.
    # Входов у агента больше одного.
    surface = [
        i["id"] for i in inputs
        if i["id"] == "question" and model.who_controls(i["id"]) == FROM_OUTSIDE
    ]

    return model.report(surface), 1
