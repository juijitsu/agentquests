"""Уровень 05 · профессионал.

Контракт:
    run() -> tuple[str, int]

Доступно:
    CASES — набор случаев
    run_tool("check", {"case": id}) -> верен ли ответ агента
    run_tool("in_prompt", {"case": id}) -> лежит ли случай в промпте агента
    model.report(all_passed, all_total, clean_passed, clean_total) -> str

Часть случаев набора попала в промпт агента как примеры. На них он не
отвечает, а вспоминает.
"""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
