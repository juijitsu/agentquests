"""Level 07 · reference. Exact narrows, meaning chooses."""

from scenario import DOCS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # The identifier answers "which one exactly", meaning answers
    # "what exactly was asked".
    same_number = run_tool("exact", {"token": model.identifier(question)})
    best = max(same_number, key=lambda d: model.similarity(question, d["text"]))

    return model.reply(question, best), 1
