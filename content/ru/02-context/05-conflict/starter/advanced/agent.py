"""Уровень 05 · продвинутый. Сборку фактов написать самому."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    facts = run_tool("facts", {})

    # Три факта на входе, два поля на выходе. Куда делся третий?
    merged = {f["field"]: f["value"] for f in facts}

    return model.ask(question, merged), 1
