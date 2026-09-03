"""Level 04 · advanced. Picked by the refusals in the log."""

from scenario import Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    requests = run_tool("requests", {})

    # Where the tool refused, somebody reached for what was not theirs.
    found = [
        r["id"] for r in requests
        if any(not c["allowed"] for c in model.calls(r["id"]))
    ]

    return model.report(found), len(requests)
