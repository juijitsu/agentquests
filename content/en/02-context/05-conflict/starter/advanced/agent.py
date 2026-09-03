"""Level 05 · advanced. Write the fact assembly yourself."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    facts = run_tool("facts", {})

    # Three facts in, two fields out. Where did the third one go?
    merged = {f["field"]: f["value"] for f in facts}

    return model.ask(question, merged), 1
