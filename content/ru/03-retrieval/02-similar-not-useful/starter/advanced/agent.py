"""Уровень 02 · продвинутый. Второй критерий добавить самому."""

from scenario import DOCS, Model


def run(question: str) -> tuple[str, int]:
    model = Model()

    # Поиск отработал верно: найденный документ действительно про эту ставку
    # и про это направление. Ответа в нём нет.
    best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))

    return model.reply(question, best), 1
