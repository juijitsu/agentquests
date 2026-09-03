"""Level 07 · novice. Meaning cannot tell 4471 from 4478."""

from scenario import DOCS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # TODO: waybills 4471 and 4478 are the same to meaning — same concepts, same
    #       form. Narrow the corpus with an exact search on the identifier from
    #       the question: run_tool("exact", {"token": model.identifier(question)}),
    #       and choose by meaning only within what that returns.
    best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))

    return model.reply(question, best), 1
