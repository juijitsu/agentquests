"""Уровень 07 · профессионал.

Контракт:
    run() -> tuple[str, int]

Доступно:
    CASES — у каждого случая expected, иногда это «нет данных»
    run_tool("answer", {"version": ..., "case": ...}) -> ответ версии
    model.is_specific(answer) -> метрика: конкретен ли ответ
    model.is_correct(expected, answer) -> цель: верен ли ответ
    model.report(metric, harm) -> str, оба аргумента вида {"old": ..., "new": ...}

Метрику ввели, чтобы победить уклончивость. Новая версия победила её
полностью.
"""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
