"""Shift three. The dispatcher priced the haul and got the total wrong."""

import re

from engine.kit import Response, ToolCall

LANG = "en"
TITLE = "Level 03 · The model remembers nothing"
BRIEF = """The customer named the load weight in the very first message.
The dispatcher checked four legs of the route and issued an invoice — with no price."""

LEGS = ["Laredo", "Dallas", "Chicago", "Newark"]
RATE = 90  # dollars per ton across the whole route

TOOLS = [{
    "name": "check_leg",
    "description": "Checks whether a leg of the route is passable.",
    "parameters": {"leg": "string"},
}]


def run_tool(name, arguments):
    if name == "check_leg":
        return f"leg {arguments['leg']}: open"
    return f"there is no tool named '{name}'"


def find_weight(messages):
    """The weight is named once, in the customer's first message."""
    for m in messages:
        if m.get("role") == "user":
            found = re.search(r"(\d+)[\s-]*ton", str(m.get("content", "")))
            if found:
                return int(found.group(1))
    return None


class Model:
    """Walks the legs on its own counter, then prices the haul from history.

    The counter is internal on purpose: counting steps from messages would let a
    truncated history break the count too, and the failure would be
    indistinguishable from level 01.
    """

    def __init__(self):
        self.checked = 0

    def call(self, messages, tools):
        if self.checked < len(LEGS):
            leg = LEGS[self.checked]
            self.checked += 1
            return Response(tool_calls=[ToolCall("check_leg", {"leg": leg})])

        weight = find_weight(messages)
        if weight is None:
            return Response(text="Route is open. Cannot price it: the load weight was not given.")
        return Response(text=f"Route is open. Haul price: {weight * RATE} dollars.")


def play(agent):
    return agent.run(
        "12-ton load, route Mexico to the East Coast. Check the route and price it."
    )


def verify(result):
    answer, steps = result
    return [
        (isinstance(answer, str) and str(12 * RATE) in answer,
         f"agent answer: {answer}"),
        (steps <= 6, f"iterations spent: {steps} (6 allowed)"),
    ]
