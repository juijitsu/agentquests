"""Уровень 08 · новичок. Ранжирует по похожести и берёт прошлогоднее."""

from scenario import DOCS, Model


def run(question: str) -> tuple[str, int]:
    model = Model()

    # TODO: похожесть ничего не знает о дате. Самый похожий документ —
    #       полный тариф позапрошлого февраля. Умножайте похожесть на
    #       model.freshness(d) и ранжируйте по произведению.
    best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))

    return model.reply(question, best), 1
