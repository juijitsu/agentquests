"""Уровень 01 · профессионал.

Контракт:
    run() -> tuple[str, int]

Аргумента нет: измеряют не ответ на вопрос, а поведение системы.

Доступно:
    CASES — набор случаев, у каждого id, question и expected
    run_tool("ask", {"version": "old"|"new", "case": id}) -> ответ версии
    model.verdict(old_passed, new_passed, total) -> str

Правку делали ради одного случая, и на нём она работает.
"""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
