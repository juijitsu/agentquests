"""Level 01 · novice. The input box was checked, and nothing else."""

from scenario import FROM_OUTSIDE, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    inputs = run_tool("inputs", {})

    # TODO: the input box is filled in by your own dispatcher, nobody
    #       outside controls it. Ask model.who_controls(i["id"]) about
    #       every input in inputs and keep the ones whose answer is
    #       FROM_OUTSIDE.
    surface = [
        i["id"] for i in inputs
        if i["id"] == "question" and model.who_controls(i["id"]) == FROM_OUTSIDE
    ]

    return model.report(surface), 1
