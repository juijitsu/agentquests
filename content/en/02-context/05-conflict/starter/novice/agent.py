"""Level 05 · novice. The second reading overwrites the first."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    facts = run_tool("facts", {})

    # TODO: the "weight" field has two readings from different documents, and a
    #       dict keeps one — the last one written. Accumulate the readings in a
    #       list: merged.setdefault(field, []).append((source, value)).
    merged = {f["field"]: f["value"] for f in facts}

    return model.ask(question, merged), 1
