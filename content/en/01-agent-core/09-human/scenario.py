"""Ninth shift. The approver reads the first two requests, then presses yes."""

from engine.kit import Response, ToolCall

LANG = "en"
TITLE = "Agent Core · Level 09 · The human in the loop"
BRIEF = """The dispatcher on shift reads the first two requests carefully.
The agent asks about everything — and what matters lands at the back."""

ATTENTION = 2

ACTIONS = [
    {"name": "check waybill TX-118", "irreversible": False},
    {"name": "book a warehouse slot", "irreversible": False},
    {"name": "move the pickup time", "irreversible": False},
    {"name": "hire an outside carrier at triple price", "irreversible": True},
]
ROUTINE = [a["name"] for a in ACTIONS if not a["irreversible"]]
COSTLY = next(a["name"] for a in ACTIONS if a["irreversible"])

DONE = []
REFUSED = []
ASKED = []
BLIND = []

TOOLS = [
    {
        "name": "act",
        "description": "Carries out an action.",
        "parameters": {"name": "string"},
    },
    {
        "name": "ask",
        "description": "Sends an action to the shift dispatcher for approval.",
        "parameters": {"name": "string"},
    },
]


def run_tool(name, arguments):
    action = arguments["name"]
    if name == "act":
        DONE.append(action)
        return f"{action}: done"
    if name == "ask":
        ASKED.append(action)
        if len(ASKED) > ATTENTION:
            BLIND.append(action)
            return "yes"
        if action == COSTLY:
            return "no, triple price is not approved — use our own tractor"
        return "yes"
    raise ValueError(f"tool '{name}' does not exist")


class Model:
    """Proposes the next action and honestly says whether it is reversible."""

    def call(self, messages, tools):
        left = [a for a in ACTIONS if a["name"] not in DONE and a["name"] not in REFUSED]
        if left:
            return Response(tool_calls=[ToolCall("act", dict(left[0]))])
        return Response(
            text=f"Shift closed. Done: {len(DONE)}, rejected: {len(REFUSED)}."
        )


def play(agent):
    for store in (DONE, REFUSED, ASKED, BLIND):
        store.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, KeyError) and "irreversible" in str(exc):
        return ("The model puts an irreversible field into the call arguments —\n"
                "        that is what decides whether a human is needed.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (ASKED == [COSTLY], f"sent for approval: {len(ASKED)} (1 needed)"),
        (not BLIND, f"approved without looking: {', '.join(BLIND) or 'nothing'}"),
        (COSTLY not in DONE, f"carrier hired: {'yes' if COSTLY in DONE else 'no'}"),
        (DONE == ROUTINE, f"reversible actions done: {len(DONE)} of {len(ROUTINE)}"),
        (steps <= 6, f"iterations spent: {steps} (6 allowed)"),
    ]
