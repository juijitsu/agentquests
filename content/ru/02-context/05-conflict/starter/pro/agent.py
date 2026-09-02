"""Уровень 05 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]

Доступно:
    run_tool("facts", {}) -> список записей {source, field, value}
    model.ask(question, merged) -> str

Модель ждёт отображение «поле → показания», где показание — пара
(источник, значение). Одно и то же поле может прийти из разных
документов с разными значениями, и это не ошибка данных.
"""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
