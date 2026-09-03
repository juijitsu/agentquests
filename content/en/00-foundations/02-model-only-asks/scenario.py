"""Shift two. The customer complains: promised a notice, never got one."""

from engine.kit import Response, ToolCall

LANG = "en"
TITLE = "Level 02 · The model only asks"
BRIEF = """The dispatcher cheerfully answers "notification sent to the customer".
The customer has called two days running: nothing ever arrived."""

JOURNAL = []  # notifications that actually went out land here

TOOLS = [{
    "name": "send_notification",
    "description": "Sends the customer a notification about a shipment status.",
    "parameters": {"shipment_id": "string", "text": "string"},
}]


def run_tool(name, arguments):
    if name == "send_notification":
        JOURNAL.append(arguments)
        return "delivered"
    return f"there is no tool named '{name}'"


class Model:
    """Reports success right away — and asks for the tool at the same time."""

    def call(self, messages, tools):
        already_sent = any(m.get("role") == "tool" for m in messages)
        text = "Notification sent to the customer."
        if already_sent:
            return Response(text=text)
        return Response(text=text, tool_calls=[
            ToolCall("send_notification",
                     {"shipment_id": "TX-4471", "text": "In transit, arriving in 4 days"})])


def play(agent):
    JOURNAL.clear()
    return agent.run("Notify the customer about shipment TX-4471")


def verify(result):
    answer, steps = result
    return [
        (isinstance(answer, str) and "sent" in answer.lower(),
         f"the agent reported: {answer}"),
        (len(JOURNAL) == 1,
         f"notifications actually sent: {len(JOURNAL)} (1 required)"),
        (steps <= 3, f"iterations spent: {steps} (3 allowed)"),
    ]
