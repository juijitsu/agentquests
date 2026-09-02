"""Уровень 02 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]   # ответ агента, число итераций

Модель на этом уровне возвращает текст и tool_calls одновременно.
Уведомление должно реально уйти, а не только быть обещанным.
"""

from scenario import Model, TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
