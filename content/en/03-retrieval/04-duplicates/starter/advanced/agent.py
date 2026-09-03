"""Level 04 · advanced. Work out what the selection is missing."""

from scenario import CHUNKS, TOP_K, Model


def run(question: str) -> tuple[str, int]:
    model = Model()
    ranked = sorted(
        CHUNKS, key=lambda c: model.similarity(question, c["text"]), reverse=True
    )

    # The ranking is correct, every chunk is fit and relevant.
    # The answer is still incomplete.
    picked = [c["text"] for c in ranked[:TOP_K]]

    return model.reply(question, picked), 1
