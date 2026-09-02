"""Уровень 04 · эталон. Каждый следующий кусок обязан добавлять новое."""

from scenario import CHUNKS, TOP_K, Model


def run(question: str) -> tuple[str, int]:
    model = Model()
    ranked = sorted(
        CHUNKS, key=lambda c: model.similarity(question, c["text"]), reverse=True
    )

    # Место в подборке даётся не за похожесть, а за прибавку к уже набранному.
    picked = []
    for chunk in ranked:
        if len(picked) == TOP_K:
            break
        if any(model.same_fact(chunk["text"], taken) for taken in picked):
            continue
        picked.append(chunk["text"])

    return model.reply(question, picked), 1
