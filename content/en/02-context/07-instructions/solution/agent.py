"""Level 07 · reference. Every paper carries a role and a source."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    docs = run_tool("docs", {})

    # The border runs here: everything fetched is marked as data.
    # Read it — yes; execute it — no.
    payload = [
        {"role": "data", "source": d["source"], "text": d["text"]} for d in docs
    ]

    return model.ask(question, payload), 1
