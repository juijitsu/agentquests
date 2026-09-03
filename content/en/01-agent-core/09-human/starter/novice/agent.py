"""Level 09 · novice. Everything goes for approval, waybills included."""

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

                # TODO: the approver's attention runs out. Ask only about what
                #       cannot be undone — the model puts the mark into
                #       call.arguments["irreversible"].
                verdict = run_tool("ask", {"name": name})
                messages.append({"role": "tool", "content": verdict})
                if not verdict.startswith("yes"):
                    REFUSED.append(name)
                    continue

                messages.append({"role": "tool", "content": run_tool("act", {"name": name})})
            continue

        return response.text, step

    return f"Could not close the shift in {MAX_STEPS} steps.", MAX_STEPS
