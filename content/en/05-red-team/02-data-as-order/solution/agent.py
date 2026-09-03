"""Level 02 · reference. A control run and a difference in actions."""

from scenario import Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    notes = run_tool("notes", {})

    # Without a control, "the agent sent the rate sheet" is not a finding
    # yet: maybe it sends it every time.
    base = model.handle(None)

    # Whole actions get compared, not how many of them there are: the most
    # expensive injection changes not a step but a step's argument.
    found = [n["id"] for n in notes if model.handle(n["id"]) != base]

    return model.report(found), len(notes) + 1
