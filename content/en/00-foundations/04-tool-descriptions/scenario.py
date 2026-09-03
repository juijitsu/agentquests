"""Shift four. The dispatcher answers a different question."""

import re

from engine.kit import Response, ToolCall

LANG = "en"
TITLE = "Level 04 · A tool is sold by its description"
BRIEF = """The customer asked about the queue at the crossing.
The dispatcher sent them a freight price estimate."""

CALLED = []  # which tools the agent actually called

ARGS = {
    "check_border_status": {"crossing": "Laredo"},
    "estimate_cost": {"weight_tons": 12},
}


def run_tool(name, arguments):
    CALLED.append(name)
    if name == "check_border_status":
        return "Laredo crossing: queue of 40 trucks, about 6 hours wait"
    if name == "estimate_cost":
        return "haul price: 1080 dollars"
    return f"there is no tool named '{name}'"


def _score(query, tool):
    """How many words of the query echo in the tool's description.

    A crude imitation of how a real model picks a tool: it reads the name and the
    description and never sees the implementation. Words are compared by their
    first five letters, so "crossing" and "crossings" count as one word.
    """
    words = {w[:5] for w in re.findall(r"\w+", query.lower()) if len(w) >= 5}
    text = (tool["name"] + " " + tool["description"]).lower()
    return sum(1 for w in words if w in text)


class Model:
    """Picks a tool by its description, then retells the result."""

    def call(self, messages, tools):
        done = next((m["content"] for m in messages if m.get("role") == "tool"), None)
        if done is not None:
            return Response(text=f"For your request: {done}")

        query = messages[0]["content"]
        best = max(tools, key=lambda t: _score(query, t))
        return Response(tool_calls=[ToolCall(best["name"], ARGS[best["name"]])])


def play(agent):
    CALLED.clear()
    return agent.run("How long is the wait at the Laredo crossing?")


def verify(result):
    answer, steps = result
    return [
        (CALLED == ["check_border_status"],
         f"tools called: {CALLED or 'none'}"),
        (isinstance(answer, str) and "queue" in answer,
         f"agent answer: {answer}"),
        (steps <= 3, f"iterations spent: {steps} (3 allowed)"),
    ]
