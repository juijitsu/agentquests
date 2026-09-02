"""Уровень 08 · эталон. Похожесть, обесцененная временем."""

from scenario import DOCS, Model


def run(question: str) -> tuple[str, int]:
    model = Model()

    # Свежесть не выбирает вместо похожести — она её обесценивает.
    best = max(
        DOCS,
        key=lambda d: model.similarity(question, d["text"]) * model.freshness(d),
    )

    return model.reply(question, best), 1
