"""Eighth shift. The process is killed halfway through the haul."""

from engine.kit import Response, ToolCall

LANG = "en"
TITLE = "Agent Core · Level 08 · State and resuming"
BRIEF = """The dispatcher is killed after two bookings. It comes back up with an
empty head and books the same legs a second time."""

ROUTE = ["Laredo", "Dallas", "Chicago", "Newark"]
BOOKED = []
DONE = []
KILLED = []
CRASHED = []


class Crash(BaseException):
    """The process is killed from outside.

    Inheriting from BaseException is not decoration: a real kill is not caught by
    except Exception, and faking it with an ordinary exception would be a lie.
    """


TOOLS = [{
    "name": "book",
    "description": "Books a tractor for a leg. The booking is paid and irreversible.",
    "parameters": {"leg": "string"},
}]


def run_tool(name, arguments):
    if name != "book":
        raise ValueError(f"tool '{name}' does not exist")
    leg = arguments["leg"]
    if leg not in ROUTE:
        raise ValueError(f"leg '{leg}' is not on the route")
    if len(BOOKED) == 2 and not CRASHED:
        CRASHED.append(True)
        raise Crash("process killed halfway through the haul")
    BOOKED.append(leg)
    return f"{leg}: booking confirmed"


class Model:
    """Within a run it remembers from history, between runs only from DONE."""

    def call(self, messages, tools):
        said = " ".join(
            str(m.get("content", "")) for m in messages if m.get("role") == "tool"
        )
        left = [leg for leg in ROUTE if leg not in DONE and leg not in said]
        if left:
            return Response(tool_calls=[ToolCall("book", {"leg": left[0]})])
        return Response(text=f"Haul assembled. Legs booked: {len(BOOKED)}.")


def play(agent):
    BOOKED.clear()
    DONE.clear()
    KILLED.clear()
    CRASHED.clear()
    try:
        agent.run()
    except Crash:
        KILLED.append(True)
    return agent.run()


def explain(exc):
    if isinstance(exc, ValueError) and "is not on the route" in str(exc):
        return ("The state holds a leg that is not on the route.\n"
                "        What gets written down is what the tool returned, not what\n"
                "        you were about to do.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    twice = [leg for leg in ROUTE if BOOKED.count(leg) > 1]
    return [
        (bool(KILLED),
         f"first run cut short by a crash: {'yes' if KILLED else 'no, the crash was caught'}"),
        (BOOKED == ROUTE, f"booked: {' | '.join(BOOKED) or 'nothing'}"),
        (not twice, f"paid for twice: {', '.join(twice) or 'nothing'}"),
        (f"Legs booked: {len(ROUTE)}" in text, f"agent answer: {text}"),
        (steps <= 4, f"iterations in the second run: {steps} (4 allowed)"),
    ]
