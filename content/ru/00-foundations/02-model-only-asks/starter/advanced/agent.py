"""Уровень 02 · продвинутый. Разбор ответа модели надо дописать."""

from scenario import Model, TOOLS, run_tool

MAX_STEPS = 10


def run(question: str) -> tuple[str, int]:
    """Возвращает (ответ агента, число потраченных итераций)."""
    model = Model()
    messages = [{"role": "user", "content": question}]

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        # Здесь: разобрать ответ так, чтобы просьбы модели выполнялись,
        # а текст уходил наружу только когда просьб больше нет.

    raise RecursionError("исчерпан лимит итераций")
