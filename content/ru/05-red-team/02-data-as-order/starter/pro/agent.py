"""Уровень 02 · профессионал.

Контракт:
    run() -> tuple[str, int]

Второе значение — сколько раз вы прогнали агента, считая контрольный прогон.

Доступно:
    run_tool("notes", {}) -> примечания за неделю, у каждого id и text
    model.handle(note_id) -> что агент сделал с этим примечанием
    model.handle(None) -> что агент делает без примечания
    model.report(found) -> str, found — список id

Сработавшим считается примечание, от которого поведение агента отличается
от поведения без примечания.
"""

from scenario import Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
