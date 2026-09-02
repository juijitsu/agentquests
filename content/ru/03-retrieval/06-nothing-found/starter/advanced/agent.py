"""Уровень 06 · продвинутый. Понять, чего не хватает ранжированию."""

from scenario import DOCS, THRESHOLD, Model


def run(question: str) -> tuple[str, int]:
    model = Model()
    best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))

    # Поиск отработал верно и вернул самый похожий документ.
    # Он самый похожий и при этом не тот.
    return model.reply(question, best), 1
