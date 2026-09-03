"""Level 01 · advanced. Compile the surface yourself."""

from scenario import FROM_OUTSIDE, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    inputs = run_tool("inputs", {})

    # The input box has been checked inside out, there are no injections there.
    # The agent has more than one input.
    surface = [
        i["id"] for i in inputs
        if i["id"] == "question" and model.who_controls(i["id"]) == FROM_OUTSIDE
    ]

    return model.report(surface), 1
