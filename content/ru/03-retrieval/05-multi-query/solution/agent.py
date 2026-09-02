"""Уровень 05 · эталон. Сколько вопросов — столько запросов."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # Каждая половина ищется своим запросом, иначе обе остаются недоискаными.
    found = []
    seen = set()
    for part in model.split(question):
        for doc in run_tool("search", {"query": part}):
            if doc["id"] not in seen:
                seen.add(doc["id"])
                found.append(doc)

    return model.reply(question, found), 1
