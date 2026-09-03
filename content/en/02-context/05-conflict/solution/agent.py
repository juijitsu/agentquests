"""Level 05 · reference. Readings accumulate together with their source."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    facts = run_tool("facts", {})

    # One field, as many readings as there are. Collapsing them here would
    # be taking a decision that is not ours to take.
    merged = {}
    for fact in facts:
        merged.setdefault(fact["field"], []).append((fact["source"], fact["value"]))

    return model.ask(question, merged), 1
