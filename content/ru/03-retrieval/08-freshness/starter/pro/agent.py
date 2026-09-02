"""Уровень 08 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]

Доступно:
    DOCS — у каждого документа есть dated
    model.similarity(left, right) -> близость по смыслу
    model.freshness(doc) -> во сколько раз документ обесценился
    model.reply(question, doc) -> str

Самый похожий документ здесь прошлогодний, а самый свежий — про другое
направление. Ни один сигнал по отдельности не даёт верного ответа.
"""

from scenario import DOCS, Model


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
