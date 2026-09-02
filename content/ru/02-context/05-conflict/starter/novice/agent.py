"""Уровень 05 · новичок. Второе показание затирает первое."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    facts = run_tool("facts", {})

    # TODO: у поля «вес» два показания из разных документов, а словарь
    #       оставляет одно — последнее записанное. Накапливайте показания
    #       списком: merged.setdefault(поле, []).append((источник, значение)).
    merged = {f["field"]: f["value"] for f in facts}

    return model.ask(question, merged), 1
