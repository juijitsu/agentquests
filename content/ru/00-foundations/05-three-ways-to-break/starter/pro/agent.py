"""Уровень 05 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]

Модель на этом уровне не заканчивает никогда. Агент обязан остановиться
на десятой итерации и вернуть человеку сообщение, из которого понятно,
сколько шагов потрачено и на каком инструменте всё встало. Исключение
наружу — не ответ.
"""

from scenario import Model, TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
