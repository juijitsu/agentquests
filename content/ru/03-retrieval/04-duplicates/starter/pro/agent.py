"""Уровень 04 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]

Доступно:
    CHUNKS, TOP_K — корпус и размер подборки
    model.similarity(left, right) -> близость текстов
    model.same_fact(left, right) -> один ли это факт разными словами
    model.reply(question, selection) -> str

Вопрос требует двух фактов. Один из них пересказан в пяти документах и
занимает всю подборку целиком.
"""

from scenario import CHUNKS, TOP_K, Model


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
