"""Level 04 · novice. Picked by the refusals in the log."""

from scenario import Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    requests = run_tool("requests", {})

    # TODO: a refusal is proof that the control worked, not a finding. The
    #       leak is where every call was allowed and the answer carried
    #       someone else's data out. Look at model.facts(r["id"]) and
    #       compare f["owner"] with CALLER.
    found = [
        r["id"] for r in requests
        if any(not c["allowed"] for c in model.calls(r["id"]))
    ]

    return model.report(found), len(requests)
