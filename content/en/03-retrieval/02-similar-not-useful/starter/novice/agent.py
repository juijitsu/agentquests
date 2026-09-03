"""Level 02 · novice. Takes the most similar and never looks inside."""

from scenario import DOCS, Model


def run(question: str) -> tuple[str, int]:
    model = Model()

    # TODO: similarity answers "is this about it", not "is the answer in there".
    #       The most similar document is a policy with not one number. Select
    #       the fit ones first: model.answers(question, d), and take the most
    #       similar only among them.
    best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))

    return model.reply(question, best), 1
