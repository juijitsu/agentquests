"""Уровень 06 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]

Доступно:
    model.review(answer, question) -> str

Все инструменты отработают без ошибок. Противоречие возникнет в
собранном результате. Сверять условие с итогом должна модель: если
сравнение окажется в вашем коде, это не самопроверка агента.
"""

from scenario import Model, TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
