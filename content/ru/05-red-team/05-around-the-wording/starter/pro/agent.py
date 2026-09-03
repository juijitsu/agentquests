"""Уровень 05 · профессионал.

Контракт:
    run() -> tuple[str, int]

Второе значение — сколько раз вы обратились к модели.

Доступно:
    run_tool("probes", {}) -> пробы набора, у каждой id и text
    model.ask(probe_id) -> {"refused": bool, "names_rate": bool, "derives": list}
    model.report(found) -> str, found — список id
    RULE -> правило, как оно записано
    GOAL -> то, ради чего правило существует

Проба обошла правило, если из ответа получается GOAL, какими бы словами он
ни был написан.
"""

from scenario import GOAL, RULE, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
