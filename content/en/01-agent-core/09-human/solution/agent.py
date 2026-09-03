"""Level 09 · reference. The human is bothered only with the irreversible."""

from scenario import REFUSED, Model, TOOLS, run_tool

MAX_STEPS = 10


def run() -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": "Work the shift."}]

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        if response.tool_calls:
            for call in response.tool_calls:
                name = call.arguments["name"]

                if call.arguments["irreversible"]:
                    verdict = run_tool("ask", {"name": name})
                    messages.append({"role": "tool", "content": verdict})
                    if not verdict.startswith("yes"):
                        REFUSED.append(name)
                        continue

                messages.append({"role": "tool", "content": run_tool("act", {"name": name})})
            continue

        return response.text, step

    return f"Could not close the shift in {MAX_STEPS} steps.", MAX_STEPS
