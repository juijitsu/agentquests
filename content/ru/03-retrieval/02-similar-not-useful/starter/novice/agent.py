"""Уровень 02 · новичок. Берёт самое похожее и не смотрит, что внутри."""

from scenario import DOCS, Model


def run(question: str) -> tuple[str, int]:
    model = Model()

    # TODO: похожесть отвечает «про то ли это», а не «есть ли там ответ».
    #       Самый похожий документ — регламент без единого числа. Отберите
    #       сперва пригодные: model.answers(question, d), и только среди них
    #       берите самый похожий.
    best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))

    return model.reply(question, best), 1
