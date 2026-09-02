"""Уровень 08 · продвинутый. Второй сигнал добавить самому."""

from scenario import DOCS, Model


def run(question: str) -> tuple[str, int]:
    model = Model()

    # Найденный документ про то самое направление и содержит ставку.
    # Ставка действует с февраля позапрошлого года.
    best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))

    return model.reply(question, best), 1
