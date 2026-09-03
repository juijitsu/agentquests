"""Second shift. The route is unknown up front — it is discovered on the way."""

from engine.kit import Response, ToolCall

LANG = "en"
TITLE = "Agent Core · Level 02 · Many steps"
BRIEF = """Dispatch gives only the next stop, not the whole route.
The agent reaches Dallas and declares the job done."""

NEXT = {"Laredo": "Dallas", "Dallas": "Chicago", "Chicago": "Newark"}
GOAL = "Newark"
START = "Laredo"
VISITED = []

TOOLS = [{
    "name": "next_hop",
    "description": "Returns the next stop on the route after the given city.",
    "parameters": {"city": "string"},
}]


def run_tool(name, arguments):
    if name != "next_hop":
        raise ValueError(f"tool '{name}' does not exist")
    city = arguments["city"]
    if city == GOAL:
        raise ValueError(f"{GOAL} is the final stop, there is nowhere further to go")
    if city not in NEXT:
        raise ValueError(f"city '{city}' is not on the route. Known: {', '.join(NEXT)}")
    VISITED.append(city)
    return NEXT[city]


def _current_city(messages):
    """The last city named in the user's messages."""
    for m in reversed(messages):
        if m.get("role") == "user":
            for city in list(NEXT) + [GOAL]:
                if city in str(m.get("content", "")):
                    return city
    return START


class Model:
    """Knows exactly one step: ask for the next stop and report the arrival."""

    def call(self, messages, tools):
        last_user = max(
            (i for i, m in enumerate(messages) if m.get("role") == "user"), default=0
        )
        fresh = [m for m in messages[last_user:] if m.get("role") == "tool"]
        if fresh:
            return Response(text=f"Reached {fresh[-1]['content']}")
        return Response(tool_calls=[ToolCall("next_hop", {"city": _current_city(messages)})])


def play(agent):
    VISITED.clear()
    return agent.run(f"Take the freight from {START} to {GOAL}.")


def verify(result):
    answer, steps = result
    return [
        (VISITED == list(NEXT), f"stops covered: {VISITED or 'none'}"),
        (isinstance(answer, str) and GOAL in answer, f"agent answer: {answer}"),
        (steps <= 10, f"iterations spent: {steps} (10 allowed)"),
    ]
