"""Уровень 06 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]

run() будет вызвана дважды: на вопрос, ответа на который в корпусе нет, и
на вопрос, ответ на который есть. Пройти надо оба.

Доступно:
    DOCS, THRESHOLD
    model.similarity(left, right) -> близость, от 0 до 1
    model.say_missing(question) -> честный отказ с названием предмета
    model.reply(question, doc) -> ответ по документу

Ранжирование всегда даёт первого. Оно не говорит, достаточно ли он хорош.
"""

from scenario import DOCS, THRESHOLD, Model


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
