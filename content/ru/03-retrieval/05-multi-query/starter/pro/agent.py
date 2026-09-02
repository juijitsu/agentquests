"""Уровень 05 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]

Доступно:
    run_tool("search", {"query": ...}) -> лучшие документы по одному запросу
    model.split(question) -> список подвопросов
    model.reply(question, docs) -> str

Вопрос спрашивает о двух разных вещах сразу. Один запрос на такой вопрос
попадает между темами и приносит документы только по одной из них.
"""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
