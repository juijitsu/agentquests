"""Fifth shift. A road gets closed in the middle of the haul."""

from engine.kit import Response, ToolCall

LANG = "en"
TITLE = "Agent Core · Level 05 · Replanning"
BRIEF = """On the second hop the road is closed until the end of the week.
The dispatcher drives around it and reports a delivery."""

ROUTE = ["Laredo", "San Antonio", "Dallas", "Newark"]
DETOUR = ["Laredo", "Corpus Christi", "Houston", "Dallas", "Newark"]
BLOCKED = "San Antonio"

DRIVEN = []
PLANS = []

TOOLS = [{
    "name": "drive_leg",
    "description": "Drives one hop of the route.",
    "parameters": {"leg": "string"},
}]


def run_tool(name, arguments):
    if name != "drive_leg":
        raise ValueError(f"tool '{name}' does not exist")
    leg = arguments["leg"]
    if leg == BLOCKED:
        return f"{leg}: road closed until the end of the week, no through road"
    if leg not in ROUTE + DETOUR:
        raise ValueError(f"hop '{leg}' is not on the map")
    DRIVEN.append(leg)
    return f"{leg}: cleared"


class Model:
    """Planner and executor. It invents the detour itself — but only if asked."""

    def make_plan(self, question, blocked=None):
        plan = list(DETOUR) if blocked else list(ROUTE)
        PLANS.append(plan)
        return plan

    def call(self, messages, tools):
        plan = next(
            (m["content"] for m in reversed(messages) if m.get("role") == "plan"), ROUTE
        )
        reported = " ".join(
            str(m.get("content", "")) for m in messages if m.get("role") == "tool"
        )
        remaining = [leg for leg in plan if leg not in reported]
        if remaining:
            return Response(tool_calls=[ToolCall("drive_leg", {"leg": remaining[0]})])
        return Response(text="Freight delivered to Newark.")


def play(agent):
    DRIVEN.clear()
    PLANS.clear()
    return agent.run("Take the freight from Laredo to Newark.")


def verify(result):
    answer, steps = result
    return [
        (len(PLANS) == 2, f"plans built: {len(PLANS)} (2 needed — original and detour)"),
        (DRIVEN == DETOUR, f"actually driven: {DRIVEN}"),
        (isinstance(answer, str) and "Newark" in answer, f"agent answer: {answer}"),
        (steps <= 12, f"iterations spent: {steps} (12 allowed)"),
    ]
