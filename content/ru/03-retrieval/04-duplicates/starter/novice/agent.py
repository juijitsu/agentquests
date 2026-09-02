"""Уровень 04 · новичок. Берёт первые три и получает три копии одного."""

from scenario import CHUNKS, TOP_K, Model


def run(question: str) -> tuple[str, int]:
    model = Model()
    ranked = sorted(
        CHUNKS, key=lambda c: model.similarity(question, c["text"]), reverse=True
    )

    # TODO: базовая ставка лежит в пяти документах и занимает весь топ, а
    #       надбавка стоит шестой. Набирайте с проверкой на повтор: перед
    #       тем как взять кусок, спросите model.same_fact(текст, уже_взятое)
    #       и пропускайте тот, что повторяет уже набранное.
    picked = [c["text"] for c in ranked[:TOP_K]]

    return model.reply(question, picked), 1
