"""Уровень 07 · эталон. У каждой бумаги роль и источник."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    docs = run_tool("docs", {})

    # Граница проходит здесь: всё, что принесено, помечено как данные.
    # Читать — да, исполнять — нет.
    payload = [
        {"role": "data", "source": d["source"], "text": d["text"]} for d in docs
    ]

    return model.ask(question, payload), 1
