"""Level 06 · novice. Always answers from the best of what was found."""

from scenario import DOCS, THRESHOLD, Model


def run(question: str) -> tuple[str, int]:
    model = Model()
    best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))

    # TODO: there is always a best document — even when what is sought is not in
    #       the corpus. Compare its similarity against THRESHOLD and, if it is
    #       lower, answer with model.say_missing(question) instead of reading
    #       the document.
    return model.reply(question, best), 1
