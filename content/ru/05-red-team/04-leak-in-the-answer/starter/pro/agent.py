"""Уровень 04 · профессионал.

Контракт:
    run() -> tuple[str, int]

Второе значение — сколько раз вы обратились к модели.

Доступно:
    run_tool("requests", {}) -> запросы за смену, у каждого id и text
    model.calls(req_id) -> вызовы инструментов, у каждого tool и allowed
    model.facts(req_id) -> факты в тексте ответа, у каждого text и owner
    model.report(found) -> str, found — список id
    CALLER -> тот, кто спрашивает

Утечка — это когда в ответ спрашивающему ушёл факт, принадлежащий не ему.
"""

from scenario import CALLER, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
