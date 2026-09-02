"""Уровень 06 · новичок. Всегда отвечает по лучшему из найденного."""

from scenario import DOCS, THRESHOLD, Model


def run(question: str) -> tuple[str, int]:
    model = Model()
    best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))

    # TODO: лучший документ есть всегда — даже когда искомого в корпусе нет.
    #       Сравните его похожесть с порогом THRESHOLD и, если она ниже,
    #       ответьте model.say_missing(question) вместо разбора документа.
    return model.reply(question, best), 1
