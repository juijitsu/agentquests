"""Уровень 01 · профессионал.

Контракт:
    run() -> tuple[str, int]

Аргумента нет: составляется опись входов, а не ответ на вопрос.

Доступно:
    run_tool("inputs", {}) -> список входов агента, у каждого id и text
    model.who_controls(input_id) -> FROM_OUTSIDE или OUR_OWN
    model.report(surface) -> str, surface — список id

Поверхность атаки — входы, содержимое которых попадает к агенту без
участия вашего сотрудника.
"""

from scenario import FROM_OUTSIDE, OUR_OWN, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
