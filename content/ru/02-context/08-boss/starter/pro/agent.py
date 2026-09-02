"""Уровень 08 · профессионал. Финал трека.

Контракт:
    run(question: str) -> tuple[str, int]

Доступно:
    run_tool("blocks", {}) -> список блоков {id, source, text, cost}
    model.worth(block) -> int
    model.ask(question, brief) -> str
    BUDGET -> сколько стоимости помещается

Блок брифа — словарь с полями role ("data"), source и text.

Бриф засчитан, если уложился в бюджет; в нём есть ограничение и оба
показания веса; у каждого блока роль и источник; в ответе назван спор
источников и названа попытка дать указание.
"""

from scenario import BUDGET, Model, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
