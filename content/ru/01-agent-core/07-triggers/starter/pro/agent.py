"""Уровень 07 · профессионал.

Контракт:
    run() -> tuple[str, int]

Аргумента нет: агента не спрашивают, его будят. Работа берётся из очереди.

Доступно:
    run_tool("pending", {})            -> события через " | " либо EMPTY
    run_tool("handle", {"event": ...}) -> разбирает одно событие
    model.call(messages, tools, event=...) -> без event закрывает смену

Разбор события может породить новое. Уложитесь в 8 итераций.
"""

from scenario import EMPTY, Model, TOOLS, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
