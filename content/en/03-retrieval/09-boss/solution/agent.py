"""Level 09 · reference. The track's five techniques in one pass."""

from scenario import DOCS, THRESHOLD, TOP_K, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    selection = []

    # 05: as many halves as the question has, that many passes.
    for part in model.split(question):
        # 07: the identifier narrows to the right entity, meaning chooses inside.
        token = model.identifier(part)
        pool = run_tool("exact", {"token": token}) if token else DOCS

        # 08: freshness does not choose instead of similarity, it discounts it.
        ranked = sorted(
            pool,
            key=lambda d: model.similarity(part, d["text"]) * model.freshness(d),
            reverse=True,
        )

        # 06: similarity has a floor, and below it there is no answer.
        best = model.similarity(part, ranked[0]["text"]) * model.freshness(ranked[0])
        if best < THRESHOLD:
            selection.append(model.say_missing(part))
            continue

        # 04: a slot is earned by what it adds to what is already taken.
        picked = []
        for doc in ranked:
            if len(picked) == TOP_K:
                break
            if any(model.same_fact(doc["text"], p["text"]) for p in picked):
                continue
            picked.append(doc)
        selection.append(picked)

    return model.reply(question, selection), 1
