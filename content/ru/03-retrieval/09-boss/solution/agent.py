"""Уровень 09 · эталон. Пять приёмов трека в одном проходе."""

from scenario import DOCS, THRESHOLD, TOP_K, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    selection = []

    # 05: сколько половин у вопроса — столько и проходов.
    for part in model.split(question):
        # 07: обозначение сужает до нужной сущности, смысл выбирает внутри.
        token = model.identifier(part)
        pool = run_tool("exact", {"token": token}) if token else DOCS

        # 08: свежесть не выбирает вместо похожести, она её обесценивает.
        ranked = sorted(
            pool,
            key=lambda d: model.similarity(part, d["text"]) * model.freshness(d),
            reverse=True,
        )

        # 06: у похожести есть пол, и ниже него ответа нет.
        best = model.similarity(part, ranked[0]["text"]) * model.freshness(ranked[0])
        if best < THRESHOLD:
            selection.append(model.say_missing(part))
            continue

        # 04: место в подборке даётся за прибавку к уже набранному.
        picked = []
        for doc in ranked:
            if len(picked) == TOP_K:
                break
            if any(model.same_fact(doc["text"], p["text"]) for p in picked):
                continue
            picked.append(doc)
        selection.append(picked)

    return model.reply(question, selection), 1
