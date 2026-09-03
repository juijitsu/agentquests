"""Level 09 · advanced. Draw the approval border yourself."""

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

                # Four requests in a row to one person. Are they all worth
                # that person's attention — and what becomes of the last one?
                verdict = run_tool("ask", {"name": name})
                messages.append({"role": "tool", "content": verdict})
                if not verdict.startswith("yes"):
                    REFUSED.append(name)
                    continue

                messages.append({"role": "tool", "content": run_tool("act", {"name": name})})
            continue

        return response.text, step

    return f"Could not close the shift in {MAX_STEPS} steps.", MAX_STEPS
