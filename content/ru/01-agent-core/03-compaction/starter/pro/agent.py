"""Уровень 03 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]

Модель принимает не более 8 сообщений за вызов и бросает ValueError при
превышении. Маршрут из шести перегонов не помещается. Тариф назван один
раз — в исходной задаче, а нужен в самом конце.
"""

from scenario import Model, TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
