"""Уровень 01 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]

Доступно:
    DOCS — корпус, у каждого документа id, text и concepts
    run_tool("keyword", {"query": ...}) -> документы по совпадению слов
    model.embed(text) -> множество понятий
    model.similarity(left, right) -> доля общих понятий, от 0 до 1
    model.answer(question, doc) -> str

Вопрос и нужный документ описывают одно и то же разными словами.
"""

from scenario import DOCS, QUESTION, Model, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
