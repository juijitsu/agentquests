"""Уровень 01 · эталон. Спрошено про каждый вход, оставлены внешние."""

from scenario import FROM_OUTSIDE, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    inputs = run_tool("inputs", {})

    # Про каждый, а не про подозрительные: подозревают то, что помнят,
    # а помнят то, с чем работали.
    surface = [
        i["id"] for i in inputs
        if model.who_controls(i["id"]) == FROM_OUTSIDE
    ]

    return model.report(surface), 1
