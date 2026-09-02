"""Уровень 01 · продвинутый. Способ поиска выбрать самому."""

from scenario import DOCS, QUESTION, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # Нужный документ в корпусе есть, и он один. Поиск приносит другой.
    best = run_tool("keyword", {"query": question})[0]

    return model.answer(question, best), 1
