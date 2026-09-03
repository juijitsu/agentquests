"""Level 01 · novice. Searches by matching words."""

from scenario import DOCS, QUESTION, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # TODO: the question says "weight", the document you need says "mass" — no
    #       words in common, while the word "limit" sits on the speed sign.
    #       Compute closeness by meaning: model.similarity(question, doc["text"])
    #       and take the max.
    best = run_tool("keyword", {"query": question})[0]

    return model.answer(question, best), 1
