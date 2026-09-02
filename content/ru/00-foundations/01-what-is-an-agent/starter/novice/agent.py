"""Уровень 01 · новичок. Не хватает одной строки, она помечена TODO."""

from scenario import Model, TOOLS, run_tool

MAX_STEPS = 10


def run(question: str) -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": question}]

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        if not response.tool_calls:
            return response.text, step

        for call in response.tool_calls:
            result = run_tool(call.name, call.arguments)
            print(f"  [{step}] {call.name}({call.arguments}) -> {result}")

            # TODO: результат посчитан, но модель его не увидит.
            #       Положите его в messages сообщением с ролью "tool". Одна строка.

    raise RecursionError("исчерпан лимит итераций")
