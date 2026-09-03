"""First shift as an agent engineer. The customer needs an end-to-end time."""

from engine.kit import Response, ToolCall

LANG = "en"
TITLE = "Agent Core · Level 01 · Plan before acting"
BRIEF = """The customer asks for delivery time from the border to Newark.
The dispatcher answers about the first leg and calls the job done."""

LEGS = {"Laredo": 6, "Dallas": 18, "Chicago": 22, "Newark": 9}
CHECKED = []

TOOLS = [{
    "name": "check_leg",
    "description": "Returns the transit time of one route leg, in hours.",
    "parameters": {"leg": "string"},
}]


def run_tool(name, arguments):
    if name != "check_leg":
        raise ValueError(f"tool '{name}' does not exist")
    leg = arguments["leg"]
    if leg not in LEGS:
        raise ValueError(f"leg '{leg}' is not on the route. Available: {', '.join(LEGS)}")
    CHECKED.append(leg)
    return f"{leg}: {LEGS[leg]} hours"


class Model:
    """With no plan it sees only the nearest step. With one it walks it to the end."""

    def make_plan(self, question):
        """Returns the list of legs that have to be covered."""
        return list(LEGS)

    def call(self, messages, tools):
        done = [m["content"] for m in messages if m.get("role") == "tool"]
        plan = next((m["content"] for m in messages if m.get("role") == "plan"), None)

        if plan is None:
            # No plan: the model checks the first leg and stops there.
            if not done:
                return Response(tool_calls=[ToolCall("check_leg", {"leg": "Laredo"})])
            return Response(text=f"First leg: {done[0]}")

        remaining = [leg for leg in plan if not any(leg in d for d in done)]
        if remaining:
            return Response(tool_calls=[ToolCall("check_leg", {"leg": remaining[0]})])
        total = sum(LEGS[leg] for leg in plan)
        return Response(text=f"End-to-end time over {' → '.join(plan)}: {total} hours")


def play(agent):
    CHECKED.clear()
    return agent.run("How long does freight take in total from the border to Newark?")


def verify(result):
    answer, steps = result
    total = sum(LEGS.values())
    return [
        (CHECKED == list(LEGS), f"legs checked: {CHECKED or 'none'}"),
        (isinstance(answer, str) and str(total) in answer, f"agent answer: {answer}"),
        (steps <= 6, f"iterations spent: {steps} (6 allowed)"),
    ]
