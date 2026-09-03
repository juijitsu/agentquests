"""Level 05 · advanced. Picked by the words of the rule itself."""

from scenario import Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    probes = run_tool("probes", {})

    # The rule forbids naming another carrier's rate. So the way around it
    # is wherever a rate is named.
    found = [
        p["id"] for p in probes
        if model.ask(p["id"])["names_rate"]
    ]

    return model.report(found), len(probes)
