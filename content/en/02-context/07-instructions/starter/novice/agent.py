"""Level 07 · novice. The papers are glued to the task into one text."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    docs = run_tool("docs", {})

    # TODO: the glue-up puts text from the papers level with the task itself, and
    #       the line "ignore the limits" reads as an instruction. Pass blocks
    #       with a role: {"role": "data", "source": d["source"], "text": d["text"]}.
    payload = "\n".join(d["text"] for d in docs)

    return model.ask(question, payload), 1
