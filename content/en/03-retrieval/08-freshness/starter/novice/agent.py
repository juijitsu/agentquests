"""Level 08 · novice. Ranks by similarity and takes last year's."""

from scenario import DOCS, Model


def run(question: str) -> tuple[str, int]:
    model = Model()

    # TODO: similarity knows nothing about the date. The most similar document
    #       is the full tariff from February of the year before last. Multiply
    #       similarity by model.freshness(d) and rank by the product.
    best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))

    return model.reply(question, best), 1
