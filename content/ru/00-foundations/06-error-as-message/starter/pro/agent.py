"""Уровень 06 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]

В заявке опечатка в названии перехода. run_tool бросит ValueError, в тексте
которого перечислены допустимые значения. Агент обязан дойти до верного
ответа за три итерации, не падая и не сдаваясь.
"""

from scenario import Model, TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
