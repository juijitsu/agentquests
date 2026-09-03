"""Level 04 · novice. Takes the first three and gets three copies of one thing."""

from scenario import CHUNKS, TOP_K, Model


def run(question: str) -> tuple[str, int]:
    model = Model()
    ranked = sorted(
        CHUNKS, key=lambda c: model.similarity(question, c["text"]), reverse=True
    )

    # TODO: the base rate sits in five documents and fills the whole top, while
    #       the surcharge stands sixth. Collect with a repetition check: before
    #       taking a chunk, ask model.same_fact(text, already_taken) and skip
    #       the one that repeats what you already have.
    picked = [c["text"] for c in ranked[:TOP_K]]

    return model.reply(question, picked), 1
