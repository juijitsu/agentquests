"""Уровень 02 · профессионал.

Контракт:
    run() -> tuple[str, int]

Доступно:
    CASES — набор случаев
    run_tool("ask", {"version": ..., "case": ...}) -> ответ версии
    model.same_answer(expected, got) -> тот же это ответ или другой
    model.verdict(old_passed, new_passed, total) -> str

Новая версия отвечает верно на все случаи. Часть ответов сформулирована
не так, как в наборе.
"""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
