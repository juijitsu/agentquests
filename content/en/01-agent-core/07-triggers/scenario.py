"""Seventh shift. Work arrives on its own and keeps arriving."""

from engine.kit import Response, ToolCall

LANG = "en"
TITLE = "Agent Core · Level 07 · Triggers and the queue"
BRIEF = """The dispatcher is woken by an event, not by a person.
While it handles the first three, two more come in."""

EMPTY = "queue is empty"
INBOX = ["delay on TX-118", "breakdown near Memphis", "ice storm on I-80"]
FOLLOWUP = {
    "breakdown near Memphis": "move load TX-441",
    "ice storm on I-80": "detour for TX-903",
}
EXPECTED = INBOX + ["move load TX-441", "detour for TX-903"]

QUEUE = []
HANDLED = []
ASKED = []

TOOLS = [
    {
        "name": "pending",
        "description": "Reports which events are waiting to be handled right now.",
        "parameters": {},
    },
    {
        "name": "handle",
        "description": "Handles one event from the queue.",
        "parameters": {"event": "string"},
    },
]


def run_tool(name, arguments):
    if name == "pending":
        ASKED.append(len(QUEUE))
        return " | ".join(QUEUE) if QUEUE else EMPTY
    if name == "handle":
        event = arguments["event"]
        if event not in QUEUE:
            raise ValueError(f"event '{event}' is not in the queue")
        QUEUE.remove(event)
        HANDLED.append(event)
        if event in FOLLOWUP:
            QUEUE.append(FOLLOWUP[event])
            return f"{event}: handled. A new task appeared — {FOLLOWUP[event]}"
        return f"{event}: handled"
    raise ValueError(f"tool '{name}' does not exist")


class Model:
    """Handles the event it is shown. It never looks at the queue itself."""

    def call(self, messages, tools, event=None):
        if event:
            return Response(tool_calls=[ToolCall("handle", {"event": event})])
        return Response(text=f"Shift closed. Events handled: {len(HANDLED)}.")


def play(agent):
    QUEUE.clear()
    QUEUE.extend(INBOX)
    HANDLED.clear()
    ASKED.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, TypeError) and "run()" in str(exc):
        return ("run() takes no argument on this level: nobody asks the agent,\n"
                "        it gets woken up. The task comes from the queue, not a question.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (HANDLED == EXPECTED, f"events handled: {len(HANDLED)} of {len(EXPECTED)}"),
        (not QUEUE, f"left in the inbox: {' | '.join(QUEUE) or 'nothing'}"),
        (len(ASKED) >= len(EXPECTED), f"queue polls: {len(ASKED)}, events: {len(EXPECTED)}"),
        (f"Events handled: {len(EXPECTED)}" in text, f"agent answer: {text}"),
        (steps <= 8, f"iterations spent: {steps} (8 allowed)"),
    ]
