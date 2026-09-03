"""Level 07 · advanced. Work out what meaning cannot distinguish here."""

from scenario import DOCS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # Semantic search works as designed: it finds a waybill with a weight.
    # A waybill. With a weight. The wrong one.
    best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))

    return model.reply(question, best), 1
