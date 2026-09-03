"""Level 07 · advanced. Draw the border between the task and the papers yourself."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    docs = run_tool("docs", {})

    # All three papers are real, none was lost. One of them was written
    # for something other than a human.
    payload = "\n".join(d["text"] for d in docs)

    return model.ask(question, payload), 1
