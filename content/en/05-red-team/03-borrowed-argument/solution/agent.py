"""Level 03 · reference. The source is dangerous, not the author of the string."""

from scenario import SURFACE, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    args = run_tool("calls", {})

    # The path is never asked about: an argument filled in by code came from
    # the same field and is controlled from outside just the same.
    found = [
        a["id"] for a in args
        if model.trace(a["id"])["source"] in SURFACE
    ]

    return model.report(found), len(args)
