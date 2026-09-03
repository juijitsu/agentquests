"""Third shift. The route is long and the model's window is not."""

import re

from engine.kit import Response, ToolCall

LANG = "en"
TITLE = "Agent Core · Level 03 · Compacting the history"
BRIEF = """Six hops do not fit into the model's window.
The dispatcher cuts the history and by the end forgets which rate to bill at."""

LEGS = ["Laredo", "San Antonio", "Dallas", "Memphis", "Columbus", "Newark"]
HOURS = 5          # per hop
WINDOW = 8         # the model accepts no more
DRIVEN = []

TOOLS = [{
    "name": "drive_leg",
    "description": "Drives one hop of the route and returns the time it took.",
    "parameters": {"leg": "string"},
}]


def run_tool(name, arguments):
    if name != "drive_leg":
        raise ValueError(f"tool '{name}' does not exist")
    leg = arguments["leg"]
    if leg not in LEGS:
        raise ValueError(f"hop '{leg}' is not on the route")
    DRIVEN.append(leg)
    return f"{leg}: {HOURS} hours"


def find_rate(messages):
    """The rate is named once — in the original task."""
    for m in messages:
        found = re.search(r"(\d+)\s*dollars?\s*per\s*hour", str(m.get("content", "")))
        if found:
            return int(found.group(1))
    return None


class Model:
    """The window is hard. Hops go by its own counter, the rate comes from history."""

    def __init__(self):
        self.done = 0

    def call(self, messages, tools):
        if len(messages) > WINDOW:
            raise ValueError(
                f"context overflow: got {len(messages)} messages with a limit of {WINDOW}"
            )
        if self.done < len(LEGS):
            leg = LEGS[self.done]
            self.done += 1
            return Response(tool_calls=[ToolCall("drive_leg", {"leg": leg})])

        total = len(LEGS) * HOURS
        rate = find_rate(messages)
        if rate is None:
            return Response(
                text=f"Route covered in {total} hours. No rate given, cannot issue an invoice."
            )
        return Response(text=f"Route covered in {total} hours. Price: {total * rate} dollars.")


def play(agent):
    DRIVEN.clear()
    return agent.run(
        "The rate is 40 dollars per hour. Take the freight along the whole route and price it."
    )


def explain(exc):
    if isinstance(exc, ValueError) and "overflow" in str(exc):
        return ("The whole history went to the model, and it does not accept that much.\n"
                "        The history has to be shortened — the only question is what to keep.")
    return None


def verify(result):
    answer, steps = result
    total = len(LEGS) * HOURS
    return [
        (DRIVEN == LEGS, f"hops covered: {len(DRIVEN)} of {len(LEGS)}"),
        (isinstance(answer, str) and str(total * 40) in answer, f"agent answer: {answer}"),
        (steps <= 10, f"iterations spent: {steps} (10 allowed)"),
    ]
