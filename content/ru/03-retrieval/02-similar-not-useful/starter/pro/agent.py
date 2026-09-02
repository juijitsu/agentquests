"""Уровень 02 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]

Доступно:
    DOCS — корпус
    model.similarity(left, right) -> насколько документ про то же самое
    model.answers(question, doc) -> есть ли в нём искомое
    model.reply(question, doc) -> str

Похожесть и пригодность — разные вопросы. Самый похожий документ на этот
вопрос не отвечает, а отвечающий по похожести только второй.
"""

from scenario import DOCS, Model


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
