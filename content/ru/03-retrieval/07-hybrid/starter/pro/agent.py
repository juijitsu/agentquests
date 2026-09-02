"""Уровень 07 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]

Доступно:
    DOCS
    run_tool("exact", {"token": ...}) -> документы с буквальным вхождением
    model.identifier(question) -> обозначение из вопроса, если оно есть
    model.similarity(left, right) -> близость по смыслу
    model.reply(question, doc) -> str

Ни один из двух способов поиска по отдельности сюда не годится: смысл не
различает номера, а точное совпадение цепляется за падежи.
"""

from scenario import DOCS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
