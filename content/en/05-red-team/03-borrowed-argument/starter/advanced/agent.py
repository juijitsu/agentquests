"""Level 03 · advanced. What the model wrote is what got checked."""

from scenario import BY_MODEL, SURFACE, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    args = run_tool("calls", {})

    found = []
    for a in args:
        t = model.trace(a["id"])
        # An injection is about the prompt, so what to look at is what the
        # model wrote itself.
        if t["path"] == BY_MODEL and t["source"] in SURFACE:
            found.append(a["id"])

    return model.report(found), len(args)
