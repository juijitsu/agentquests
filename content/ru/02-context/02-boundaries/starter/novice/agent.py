"""Уровень 02 · новичок. Строки отобраны верно и обезличены."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    lines = run_tool("about", {"topic": model.topic(question)}).split(" | ")

    # TODO: отбор вытащил строки из тарифов и оставил их без подписи —
    #       по ним не понять, чья надбавка чья. Спросите источник каждой
    #       строки через run_tool("source", {"line": line}) и склейте
    #       подпись со строкой: f"{who}: {line}".
    blocks = lines

    return model.ask(question, blocks), 1
