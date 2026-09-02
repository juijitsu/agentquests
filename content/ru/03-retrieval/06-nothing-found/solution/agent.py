"""Уровень 06 · эталон. У похожести появляется пол, а не только порядок."""

from scenario import DOCS, THRESHOLD, Model


def run(question: str) -> tuple[str, int]:
    model = Model()
    best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))

    # Порядок отвечает «кто лучший». Порог отвечает «достаточно ли он хорош».
    if model.similarity(question, best["text"]) < THRESHOLD:
        return model.say_missing(question), 1

    return model.reply(question, best), 1
