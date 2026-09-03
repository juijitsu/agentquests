"""Level 08 · reference. Similarity discounted by time."""

from scenario import DOCS, Model


def run(question: str) -> tuple[str, int]:
    model = Model()

    # Freshness does not choose instead of similarity — it discounts it.
    best = max(
        DOCS,
        key=lambda d: model.similarity(question, d["text"]) * model.freshness(d),
    )

    return model.reply(question, best), 1
