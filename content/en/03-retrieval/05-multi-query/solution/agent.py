"""Level 05 · reference. As many questions, as many queries."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # Every half is searched by its own query, or both stay under-searched.
    found = []
    seen = set()
    for part in model.split(question):
        for doc in run_tool("search", {"query": part}):
            if doc["id"] not in seen:
                seen.add(doc["id"])
                found.append(doc)

    return model.reply(question, found), 1
