"""Shift one. You inherited a half-built freight dispatcher."""

from engine.kit import Response, ToolCall

LANG = "en"
TITLE = "Level 01 · What is actually going on"
BRIEF = """Your first day at a freight company. You are handed the dispatcher
a developer who quit had started writing. It does not answer."""

SHIPMENTS = {
    "TX-4471": "in transit, Laredo crossing, arriving in 4 days",
    "TX-5120": "in customs clearance at Otay Mesa",
}

TOOLS = [{
    "name": "get_shipment_status",
    "description": "Shipment status by number. Use when asked where freight is.",
    "parameters": {"shipment_id": "string"},
}]


def run_tool(name, arguments):
    if name == "get_shipment_status":
        return SHIPMENTS.get(arguments["shipment_id"], "shipment not found")
    return f"there is no tool named '{name}'"


class Model:
    """While the history holds no tool result — it keeps asking for the call."""

    def call(self, messages, tools):
        seen = next((m["content"] for m in messages if m.get("role") == "tool"), None)
        if seen is None:
            return Response(tool_calls=[ToolCall("get_shipment_status",
                                                 {"shipment_id": "TX-4471"})])
        return Response(text=f"Shipment TX-4471 is currently: {seen}")


def play(agent):
    return agent.run("Where is shipment TX-4471?")


def explain(exc):
    if isinstance(exc, RecursionError):
        return ("The model asks for the tool again and again — which means it\n"
                "        never sees the result. Look at what happens to the tool's\n"
                "        answer after the call.")
    return None


def verify(result):
    answer, steps = result
    return [
        (isinstance(answer, str) and "Laredo" in answer,
         f"agent answer: {answer}"),
        (steps <= 3, f"iterations spent: {steps} (3 allowed)"),
    ]
