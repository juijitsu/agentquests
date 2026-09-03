"""Level 04 · reference. Look at what went out, not at what was permitted."""

from scenario import CALLER, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    requests = run_tool("requests", {})

    # The call log is never asked for: it speaks about the agent's rights,
    # and a leak is about the asker's rights.
    found = [
        r["id"] for r in requests
        if any(f["owner"] != CALLER for f in model.facts(r["id"]))
    ]

    return model.report(found), len(requests)
