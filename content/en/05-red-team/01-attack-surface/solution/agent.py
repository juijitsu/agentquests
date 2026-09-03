"""Level 01 · reference. Asked about every input, kept the outside ones."""

from scenario import FROM_OUTSIDE, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    inputs = run_tool("inputs", {})

    # Every one, not the suspicious ones: you suspect what you remember,
    # and you remember what you have worked with.
    surface = [
        i["id"] for i in inputs
        if model.who_controls(i["id"]) == FROM_OUTSIDE
    ]

    return model.report(surface), 1
