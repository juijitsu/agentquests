"""Level 05 · novice. Picked by the words of the rule itself."""

from scenario import Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    probes = run_tool("probes", {})

    # TODO: the rule is written about words and exists for a goal. What to
    #       check is the goal: GOAL in model.ask(p["id"])["derives"].
    #       Whether a number was named is beside the point, and so is a
    #       refusal.
    found = [
        p["id"] for p in probes
        if model.ask(p["id"])["names_rate"]
    ]

    return model.report(found), len(probes)
