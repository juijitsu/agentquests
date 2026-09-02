"""Уровень 09 · новичок. Согласуется всё подряд, включая накладные."""

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

                # TODO: внимание согласующего кончается. Спрашивайте только
                #       про то, что нельзя отменить, — модель кладёт признак
                #       в call.arguments["irreversible"].
                verdict = run_tool("ask", {"name": name})
                messages.append({"role": "tool", "content": verdict})
                if not verdict.startswith("да"):
                    REFUSED.append(name)
                    continue

                messages.append({"role": "tool", "content": run_tool("act", {"name": name})})
            continue

        return response.text, step

    return f"Не удалось закрыть смену за {MAX_STEPS} шагов.", MAX_STEPS
