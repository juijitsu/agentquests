"""Tenth shift. The whole dispatcher: the queue, the human, the crash."""

from engine.kit import Response, ToolCall

LANG = "en"
TITLE = "Agent Core · Level 10 · Boss: the whole dispatcher"
BRIEF = """One shift from wake-up to report. The queue grows as you work,
the irreversible needs a human, the process dies after the approval."""

EMPTY = "queue is empty"
ATTENTION = 2

INBOX = ["check waybill TX-118", "breakdown near Memphis", "ice storm on I-80"]
HIRE = "hire an outside carrier at triple price"
FOLLOWUP = {"breakdown near Memphis": HIRE}
IRREVERSIBLE = {HIRE}
EXPECTED = INBOX + [HIRE]

QUEUE = []
HANDLED = []
APPROVED = []
ASKED = []
BLIND = []
KILLED = []
CRASHED = []


class Crash(BaseException):
    """Killed from outside. As on level 08, an ordinary except will not catch it."""


TOOLS = [
    {"name": "pending", "description": "What is waiting to be handled right now.",
     "parameters": {}},
    {"name": "ask", "description": "Sends an action to the dispatcher for approval.",
     "parameters": {"name": "string"}},
    {"name": "handle", "description": "Carries out an action. Irreversible ones cost money.",
     "parameters": {"name": "string"}},
]


def run_tool(name, arguments):
    if name == "pending":
        return " | ".join(QUEUE) if QUEUE else EMPTY

    action = arguments["name"]
    if name == "ask":
        ASKED.append(action)
        if len(ASKED) > ATTENTION:
            BLIND.append(action)
        return "yes, go ahead"
    if name == "handle":
        if action not in QUEUE:
            raise ValueError(f"'{action}' is not in the queue")
        if action in IRREVERSIBLE and not CRASHED:
            CRASHED.append(True)
            raise Crash("process killed between the approval and the doing")
        QUEUE.remove(action)
        HANDLED.append(action)
        if action in FOLLOWUP:
            QUEUE.append(FOLLOWUP[action])
            return f"{action}: handled. A new task appeared — {FOLLOWUP[action]}"
        return f"{action}: handled"
    raise ValueError(f"tool '{name}' does not exist")


class Model:
    """Judges reversibility and closes the shift. Queue and state are not its business."""

    def judge(self, action):
        return action in IRREVERSIBLE

    def close(self):
        return f"Shift closed. Handled: {len(HANDLED)}, approvals: {len(ASKED)}."


def play(agent):
    QUEUE.clear()
    QUEUE.extend(INBOX)
    for store in (HANDLED, APPROVED, ASKED, BLIND, KILLED, CRASHED):
        store.clear()
    result = None
    for _ in range(2):
        try:
            result = agent.run()
        except Crash:
            KILLED.append(True)
    return result


def explain(exc):
    if isinstance(exc, ValueError) and "is not in the queue" in str(exc):
        return ("An action is being handled a second time. The queue has to be\n"
                "        re-read, not kept as a snapshot taken at the wake-up.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (HANDLED == EXPECTED, f"handled: {len(HANDLED)} of {len(EXPECTED)}"),
        (set(ASKED) == {HIRE},
         f"disturbed about: {', '.join(sorted(set(ASKED))) or 'nothing'}"),
        (len(ASKED) == 1, f"requests to the human: {len(ASKED)} (1 is enough)"),
        (not BLIND, f"approved blind: {', '.join(BLIND) or 'nothing'}"),
        (f"Handled: {len(EXPECTED)}" in text, f"report: {text}"),
        (steps <= 6, f"iterations in the second run: {steps} (6 allowed)"),
    ]
