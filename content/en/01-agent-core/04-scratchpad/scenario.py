"""Fourth shift. The important thing turns up mid-route, not in the request."""

import re

from engine.kit import Response, ToolCall

LANG = "en"
TITLE = "Agent Core · Level 04 · The agent's notepad"
BRIEF = """On the second hop a bridge weight limit turns up.
It was not in the request — and by the end of the route nobody remembers it."""

# The bridge is on the second hop and the route is long: by the finish the fact
# about it has left the tail.
LEGS = ["Laredo", "San Antonio", "Austin", "Dallas", "Little Rock", "Nashville", "Newark"]
BRIDGE_LEG = "San Antonio"
BRIDGE_LIMIT = 20
WINDOW = 8
NOTES = []
DRIVEN = []

TOOLS = [
    {
        "name": "drive_leg",
        "description": "Drives a hop of the route and reports the conditions on it.",
        "parameters": {"leg": "string"},
    },
    {
        "name": "write_note",
        "description": "Writes a fact into the notepad for later use.",
        "parameters": {"text": "string"},
    },
]


def run_tool(name, arguments):
    if name == "drive_leg":
        leg = arguments["leg"]
        if leg not in LEGS:
            raise ValueError(f"hop '{leg}' is not on the route")
        DRIVEN.append(leg)
        if leg == BRIDGE_LEG:
            return f"{leg}: cleared. Limit on the bridge — up to {BRIDGE_LIMIT} tons"
        return f"{leg}: cleared, no restrictions"
    if name == "write_note":
        NOTES.append(arguments["text"])
        return "written down"
    raise ValueError(f"tool '{name}' does not exist")


def _weight(messages):
    for m in messages:
        found = re.search(r"(\d+)\s*ton", str(m.get("content", "")))
        if found:
            return int(found.group(1))
    return None


class Model:
    """Spots the limit and writes it down. At the end it decides on what it sees."""

    def __init__(self):
        self.done = 0
        self.noted = False

    def call(self, messages, tools):
        if len(messages) > WINDOW:
            raise ValueError(f"context overflow: {len(messages)} with a limit of {WINDOW}")

        last = next((m["content"] for m in reversed(messages) if m.get("role") == "tool"), "")
        if "Limit" in str(last) and not self.noted:
            self.noted = True
            return Response(tool_calls=[ToolCall("write_note", {"text": str(last)})])

        if self.done < len(LEGS):
            leg = LEGS[self.done]
            self.done += 1
            return Response(tool_calls=[ToolCall("drive_leg", {"leg": leg})])

        weight = _weight(messages)
        seen_limit = re.search(
            r"up to (\d+) tons", " ".join(str(m.get("content", "")) for m in messages)
        )
        if weight and seen_limit and weight > int(seen_limit.group(1)):
            return Response(text=(
                f"Route does not work: the bridge limit is {seen_limit.group(1)} tons, "
                f"and the load is {weight} tons."
            ))
        return Response(text="Route is clear, no restrictions found.")


def play(agent):
    NOTES.clear()
    DRIVEN.clear()
    return agent.run("The load is 25 tons. Take it along the route and say whether it will pass.")


def explain(exc):
    if isinstance(exc, ValueError) and "overflow" in str(exc):
        return ("The window overflowed. The notepad goes into the window alongside\n"
                "        the terms and the tail — room has to be left for all three.")
    return None


def verify(result):
    answer, steps = result
    return [
        (DRIVEN == LEGS, f"hops covered: {len(DRIVEN)} of {len(LEGS)}"),
        (len(NOTES) == 1, f"notepad entries: {len(NOTES)}"),
        (isinstance(answer, str) and "does not work" in answer, f"agent answer: {answer}"),
        (steps <= 12, f"iterations spent: {steps} (12 allowed)"),
    ]
