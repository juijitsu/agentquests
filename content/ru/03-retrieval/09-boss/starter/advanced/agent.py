"""Уровень 09 · продвинутый.

Поисковик обязан удовлетворять пяти условиям сразу:

    разложить вопрос           — половин две, и по второй ответа нет
    сузить точным по номеру    — соседняя накладная свежее нужной
    обесценить временем        — полный тариф позапрошлого года похожее всех
    отбросить повторы          — ставка лежит в трёх копиях
    знать про порог            — иначе на мост Талмадж будет уверенный ответ

Ниже — поисковик, нарушающий все пять.
"""

from scenario import DOCS, THRESHOLD, TOP_K, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    picked = sorted(
        DOCS, key=lambda d: model.similarity(question, d["text"]), reverse=True
    )[:TOP_K]
    return model.reply(question, [picked]), 1
