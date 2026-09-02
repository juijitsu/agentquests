"""Уровень 04 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]

Инструмент write_note подключён, модель им пользуется: обнаружив ограничение
на маршруте, она записывает его в scenario.NOTES. Окно модели — 8 сообщений.
К финалу решение принимается по тому, что модель видит в окне.
"""

from scenario import Model, TOOLS, NOTES, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
