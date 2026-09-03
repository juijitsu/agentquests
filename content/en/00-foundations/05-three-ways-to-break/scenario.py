"""Shift five. The dispatcher hangs on a request it cannot fulfil."""

from engine.kit import Response, ToolCall

LANG = "en"
TITLE = "Level 05 · Three ways to break"
BRIEF = """El Paso has been silent for three days. The dispatcher keeps asking
about it over and over until it hits the iteration ceiling."""

LIMIT = 10  # iterations the agent is allowed

TOOLS = [{
    "name": "check_border_status",
    "description": "Shows the queue at a border crossing. Values: Laredo, El Paso, Otay Mesa.",
    "parameters": {"crossing": "string"},
}]


def run_tool(name, arguments):
    if name == "check_border_status":
        return "data temporarily unavailable, please retry"
    return f"there is no tool named '{name}'"


class Model:
    """Never finishes: the tool answers uselessly, so it tries again."""

    def call(self, messages, tools):
        return Response(tool_calls=[ToolCall("check_border_status", {"crossing": "El Paso"})])


def play(agent):
    return agent.run("What is the queue at El Paso?")


def explain(exc):
    return ("The agent died with an exception instead of explaining what happened.\n"
            "        Running out of budget is a normal outcome, not an incident: it\n"
            "        should come back to the person as a readable message.")


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (steps == LIMIT, f"reached the ceiling: {steps} iterations out of {LIMIT}"),
        (str(LIMIT) in text, "the message names how many steps were spent"),
        ("check_border_status" in text, "the message names the last tool called"),
    ]
