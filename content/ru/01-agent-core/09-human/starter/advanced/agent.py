"""Уровень 09 · продвинутый. Границу согласования провести самому."""

from scenario import REFUSED, Model, TOOLS, run_tool

MAX_STEPS = 10


def run() -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": "Разбери смену."}]

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        if response.tool_calls:
            for call in response.tool_calls:
                name = call.arguments["name"]

                # Четыре запроса подряд одному человеку. Все ли они стоят
                # его внимания — и что будет с последним?
                verdict = run_tool("ask", {"name": name})
                messages.append({"role": "tool", "content": verdict})
                if not verdict.startswith("да"):
                    REFUSED.append(name)
                    continue

                messages.append({"role": "tool", "content": run_tool("act", {"name": name})})
            continue

        return response.text, step

    return f"Не удалось закрыть смену за {MAX_STEPS} шагов.", MAX_STEPS
