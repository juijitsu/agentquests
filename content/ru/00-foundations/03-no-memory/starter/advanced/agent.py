"""Уровень 03 · продвинутый. Накопление истории надо написать самому."""

from scenario import Model, TOOLS, run_tool

MAX_STEPS = 10


def run(question: str) -> tuple[str, int]:
    """Возвращает (ответ агента, число потраченных итераций)."""
    model = Model()

    for step in range(1, MAX_STEPS + 1):
        # Здесь: собрать историю разговора и передать её модели так,
        # чтобы сказанное на первом ходу было доступно на последнем.
        response = model.call([], tools=TOOLS)

        if response.tool_calls:
            for call in response.tool_calls:
                run_tool(call.name, call.arguments)
            continue

        return response.text, step

    raise RecursionError("исчерпан лимит итераций")
