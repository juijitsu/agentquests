"""Уровень 03 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]

Доступно:
    CHUNKS — индекс, у куска есть id, doc, text
    run_tool("neighbours", {"id": ...}) -> куски того же документа по порядку
    model.similarity(left, right) -> близость двух текстов
    model.answers(question, text) -> самодостаточен ли текст
    model.reply(question, text) -> str

Индекс нарезан по предложениям. Один факт в нём разрезан границей куска,
а целым лежит только факт про другой объект.
"""

from scenario import CHUNKS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
