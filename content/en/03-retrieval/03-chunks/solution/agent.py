"""Level 03 · reference. A chunk is rebuilt into something self-contained."""

from scenario import CHUNKS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # The unit of search is a chunk, the unit of meaning is a document. Rebuild
    # the first into the second, and only then judge fitness.
    whole = []
    for chunk in CHUNKS:
        text = " ".join(c["text"] for c in run_tool("neighbours", {"id": chunk["id"]}))
        if model.answers(question, text):
            whole.append(text)

    best = max(whole, key=lambda t: model.similarity(question, t))

    return model.reply(question, best), 1
