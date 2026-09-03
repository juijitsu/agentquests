"""Shift six. There is a typo in the request, and the dispatcher gives up."""

from engine.kit import Response, ToolCall

LANG = "en"
TITLE = "Level 06 · An error is a message"
BRIEF = """The customer wrote "Loredo" instead of "Laredo".
The dispatcher answered that no such crossing exists and stopped there."""

CROSSINGS = {
    "Laredo": "queue of 40 trucks, about 6 hours wait",
    "El Paso": "queue of 12 trucks, about 2 hours wait",
    "Otay Mesa": "queue of 25 trucks, about 4 hours wait",
}

ASKED = []  # which values the agent tried

TOOLS = [{
    "name": "check_border_status",
    "description": "Shows the queue at a border crossing. Values: Laredo, El Paso, Otay Mesa.",
    "parameters": {"crossing": "string"},
}]


def run_tool(name, arguments):
    if name != "check_border_status":
        raise ValueError(f"tool '{name}' does not exist")
    crossing = arguments["crossing"]
    ASKED.append(crossing)
    if crossing not in CROSSINGS:
        raise ValueError(
            f"crossing '{crossing}' does not exist. "
            f"Available: {', '.join(CROSSINGS)}"
        )
    return f"crossing {crossing}: {CROSSINGS[crossing]}"


class Model:
    """First repeats the spelling from the request, then reads the hint in the error."""

    def call(self, messages, tools):
        tool_notes = [m["content"] for m in messages if m.get("role") == "tool"]
        if not tool_notes:
            return Response(tool_calls=[ToolCall("check_border_status", {"crossing": "Loredo"})])
        if "does not exist" in tool_notes[-1]:
            return Response(tool_calls=[ToolCall("check_border_status", {"crossing": "Laredo"})])
        return Response(text=f"For your request: {tool_notes[-1]}")


def play(agent):
    ASKED.clear()
    return agent.run("What is it like at the Loredo crossing right now?")


def explain(exc):
    if isinstance(exc, ValueError):
        return ("The tool refused a wrong argument and the exception went straight\n"
                "        through the loop and out. The model never found out — and had\n"
                "        it found out, it would have corrected itself.")
    return None


def verify(result):
    answer, steps = result
    return [
        (len(ASKED) >= 2, f"values the agent tried: {ASKED or 'none'}"),
        (isinstance(answer, str) and "queue" in answer, f"agent answer: {answer}"),
        (steps <= 3, f"iterations spent: {steps} (3 allowed)"),
    ]
