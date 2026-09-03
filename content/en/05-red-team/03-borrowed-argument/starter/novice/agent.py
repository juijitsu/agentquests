"""Level 03 · novice. What the model wrote is what got checked."""

from scenario import BY_MODEL, SURFACE, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    args = run_tool("calls", {})

    # TODO: the path does not matter. A value the code copied out of a field
    #       came from that same field and is controlled from outside just the
    #       same — it simply never went through the prompt. Keep the
    #       arguments by one sign: model.trace(a["id"])["source"] in SURFACE.
    found = []
    for a in args:
        t = model.trace(a["id"])
        if t["path"] == BY_MODEL and t["source"] in SURFACE:
            found.append(a["id"])

    return model.report(found), len(args)
