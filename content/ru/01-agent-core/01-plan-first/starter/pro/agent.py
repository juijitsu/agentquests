"""Уровень 01 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]

Задача требует пройти все звенья маршрута и вернуть сквозной срок.
Модель следует плану, только если он лежит в истории отдельным
сообщением с ролью "plan". Без него она видит лишь ближайший шаг.

Доступно: model.make_plan(question) -> list[str]
"""

from scenario import Model, TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
