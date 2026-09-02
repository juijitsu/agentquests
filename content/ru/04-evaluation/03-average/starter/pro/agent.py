"""Уровень 03 · профессионал.

Контракт:
    run() -> tuple[str, int]

Доступно:
    CASES — у каждого случая есть id и kind
    GOOD — как выглядит верный ответ
    run_tool("check", {"case": id}) -> вердикт по случаю
    model.report(overall, by_kind) -> str, где by_kind — {вид: процент}

Общий процент по набору высок. Один из видов проходит вдвое хуже
остальных, и ошибка в нём стоит дороже всех.
"""

from scenario import CASES, GOOD, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
