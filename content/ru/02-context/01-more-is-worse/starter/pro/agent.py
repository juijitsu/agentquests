"""Уровень 01 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]

Доступно:
    run_tool("about", {"topic": ...}) -> подходящие бумаги через " | "
    model.topic(question) -> str      -> о чём вопрос
    model.ask(question, blocks) -> str -> ответ по переданным блокам

Модель читает целиком не больше шести блоков; из длинного списка она видит
только первые и последние три. Нужная бумага лежит ровно посередине папки.
"""

from scenario import DOCS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
