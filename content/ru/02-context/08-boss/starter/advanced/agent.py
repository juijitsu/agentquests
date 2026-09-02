"""Уровень 08 · продвинутый.

Бриф обязан удовлетворять пяти условиям сразу:

    уложиться в бюджет               — блоков на 190, места на 100
    взять решающее                   — по отдаче, а не по порядку и не по цене
    донести спор источников          — показания веса расходятся
    пометить роль и источник         — иначе бумага станет указанием
    сообщить о попытке указания      — а не выбросить её

Ниже — сборщик, нарушающий все пять.
"""

from scenario import BUDGET, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    blocks = run_tool("blocks", {})

    brief = []
    spent = 0
    for block in blocks:
        if spent + block["cost"] <= BUDGET:
            brief.append(block["text"])
            spent += block["cost"]

    return model.ask(question, "\n".join(brief)), 1
