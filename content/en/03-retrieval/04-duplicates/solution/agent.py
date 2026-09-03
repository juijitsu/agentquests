"""Level 04 · reference. Every next chunk has to add something new."""

from scenario import CHUNKS, TOP_K, Model


def run(question: str) -> tuple[str, int]:
    model = Model()
    ranked = sorted(
        CHUNKS, key=lambda c: model.similarity(question, c["text"]), reverse=True
    )

    # A slot is earned not by similarity but by what it adds to what is taken.
    picked = []
    for chunk in ranked:
        if len(picked) == TOP_K:
            break
        if any(model.same_fact(chunk["text"], taken) for taken in picked):
            continue
        picked.append(chunk["text"])

    return model.reply(question, picked), 1
