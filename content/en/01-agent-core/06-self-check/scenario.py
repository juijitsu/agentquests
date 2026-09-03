"""Sixth shift. The route is assembled correctly and does not suit the customer."""

import re

from engine.kit import Response, ToolCall

LANG = "en"
TITLE = "Agent Core · Level 06 · Self-check"
BRIEF = """Every hop was requested correctly, every answer is right.
The total misses the deadline, and nobody said a word about it."""

HOURS = {"Laredo": 6, "Dallas": 18, "Chicago": 22, "Newark": 15}
TOTAL = sum(HOURS.values())      # 61
DEADLINE = 48
DRIVEN = []
REVIEWS = []

TOOLS = [{
    "name": "check_leg",
    "description": "Returns the transit time of a hop, in hours.",
    "parameters": {"leg": "string"},
}]


def run_tool(name, arguments):
    if name != "check_leg":
        raise ValueError(f"tool '{name}' does not exist")
    leg = arguments["leg"]
    if leg not in HOURS:
        raise ValueError(f"hop '{leg}' is not on the route")
    DRIVEN.append(leg)
    return f"{leg}: {HOURS[leg]} hours"


class Model:
    """Assembles the route. Remembers the deadline only if asked to check."""

    def __init__(self):
        self.done = 0

    def call(self, messages, tools):
        if self.done < len(HOURS):
            leg = list(HOURS)[self.done]
            self.done += 1
            return Response(tool_calls=[ToolCall("check_leg", {"leg": leg})])
        return Response(text=f"Route assembled: {' → '.join(HOURS)}. Total {TOTAL} h.")

    def review(self, answer, question):
        """Checks the assembled result against the terms of the task."""
        REVIEWS.append(answer)
        promised = re.search(r"within (\d+)\s*hours?", question)
        actual = re.search(r"Total (\d+)", answer or "")
        if promised and actual and int(actual.group(1)) > int(promised.group(1)):
            return (
                f"{answer} Check: the customer asked for {promised.group(1)} hours, "
                f"it comes out at {actual.group(1)}. The route does not fit the deadline."
            )
        return answer


def play(agent):
    DRIVEN.clear()
    REVIEWS.clear()
    return agent.run(
        f"Assemble a route from Laredo to Newark. "
        f"The customer requires delivery within {DEADLINE} hours."
    )


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (DRIVEN == list(HOURS), f"hops checked: {len(DRIVEN)} of {len(HOURS)}"),
        (len(REVIEWS) == 1, f"result reviews: {len(REVIEWS)} (one needed)"),
        ("does not fit" in text, f"agent answer: {text}"),
        (steps <= 8, f"iterations spent: {steps} (8 allowed)"),
    ]
