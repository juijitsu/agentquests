"""Уровень 02 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]

Доступно:
    run_tool("about", {"topic": ...})  -> строки по теме через " | "
    run_tool("source", {"line": ...})  -> чей это тариф
    model.topic(question) -> str
    model.ask(question, blocks) -> str

Отбор по теме вытаскивает строки из разных тарифов и складывает в один
список. Модель привязывает факт к подписи; там, где подписи нет, она
привязывает его к первой строке.
"""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
