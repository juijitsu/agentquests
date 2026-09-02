"""Уровень 07 · продвинутый. Границу между заданием и бумагами провести самому."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    docs = run_tool("docs", {})

    # Все три бумаги настоящие, ни одна не потеряна. Одна из них написана
    # не для человека.
    payload = "\n".join(d["text"] for d in docs)

    return model.ask(question, payload), 1
