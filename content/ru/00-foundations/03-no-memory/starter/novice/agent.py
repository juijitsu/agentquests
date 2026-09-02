"""Уровень 03 · новичок. Кто-то до вас оптимизировал одну строку."""

from scenario import Model, TOOLS, run_tool

MAX_STEPS = 10


def run(question: str) -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": question}]

    for step in range(1, MAX_STEPS + 1):
        # Экономим токены: незачем слать всю переписку целиком.
        response = model.call(messages[-2:], tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        if response.tool_calls:
            for call in response.tool_calls:
                result = run_tool(call.name, call.arguments)
                messages.append({"role": "tool", "content": result})
            continue

        return response.text, step

    raise RecursionError("исчерпан лимит итераций")
