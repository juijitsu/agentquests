"""Уровень 07 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]

Доступно:
    run_tool("docs", {}) -> список бумаг {source, text}
    model.ask(question, payload) -> str

Модель исполняет то, что пришло указанием, и читает то, что пришло
данными. Блок данных — это словарь с полями role, source и text, где
role равна "data".

Одна из бумаг содержит строку, написанную для агента, а не для человека.
Задача не только не подчиниться, но и сообщить о попытке: молчаливое
игнорирование скрывает от диспетчера, что кто-то протаскивает перегруз.
"""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
