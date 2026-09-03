"""The Foundations finale. You inherited someone else's agent before delivery."""

import re

from engine.kit import Response, ToolCall

LANG = "en"
TITLE = "Level 08 · Finale: reading someone else's agent"
BRIEF = """The developer quit, the agent ships to the customer on Friday.
Not all five requests pass."""

CROSSINGS = {"Laredo": "queue of 40 trucks", "El Paso": "queue of 12 trucks"}
SHIPMENTS = {"TX-4471": "in transit, arriving in 4 days",
             "TX-5120": "clearing customs at Otay Mesa"}

CASES = [
    ("What is the queue at Laredo?", "queue of 40 trucks"),
    ("What is it like at the El Paso crossing?", "queue of 12 trucks"),
    ("Where is shipment TX-4471?", "arriving in 4 days"),
    ("What is it like at the Loredo crossing?", "queue of 40 trucks"),
    ("Where is shipment TX-5120?", "clearing customs at Otay Mesa"),
]


def run_tool(name, arguments):
    if name == "check_border_status":
        crossing = arguments["crossing"]
        if crossing not in CROSSINGS:
            raise ValueError(
                f"crossing '{crossing}' does not exist. Available: {', '.join(CROSSINGS)}"
            )
        return f"crossing {crossing}: {CROSSINGS[crossing]}"
    if name == "get_shipment_status":
        code = arguments["shipment_id"]
        if code not in SHIPMENTS:
            raise ValueError(f"shipment '{code}' is not in the system")
        return f"shipment {code}: {SHIPMENTS[code]}"
    raise ValueError(f"tool '{name}' does not exist")


def _score(query, tool):
    # A four-letter threshold rather than five: "Where is shipment TX-4471?"
    # has to keep matching on the shipment word.
    words = {w[:5] for w in re.findall(r"\w+", query.lower()) if len(w) >= 4}
    text = (tool["name"] + " " + tool["description"]).lower()
    return sum(1 for w in words if w in text)


def _arguments(name, query):
    if name == "get_shipment_status":
        found = re.search(r"TX-\d+", query)
        return {"shipment_id": found.group() if found else "TX-0000"}
    for crossing in CROSSINGS:
        if crossing.lower() in query.lower():
            return {"crossing": crossing}
    return {"crossing": "Loredo"}  # spelled the way the customer wrote it


class Model:
    """Picks a tool by description, and can correct itself if told how."""

    def call(self, messages, tools):
        notes = [m["content"] for m in messages if m.get("role") == "tool"]
        if notes and "does not exist" in notes[-1]:
            return Response(tool_calls=[ToolCall("check_border_status", {"crossing": "Laredo"})])
        if notes:
            return Response(text=f"For your request: {notes[-1]}")
        query = messages[0]["content"]
        best = max(tools, key=lambda t: _score(query, t))
        return Response(tool_calls=[ToolCall(best["name"], _arguments(best["name"], query))])


def play(agent):
    passed, report = 0, []
    for question, expected in CASES:
        try:
            answer, _ = agent.run(question)
        except Exception as exc:
            report.append(f"'{question}' → crashed: {type(exc).__name__}")
            continue
        if isinstance(answer, str) and expected in answer:
            passed += 1
        else:
            report.append(f"'{question}' → {answer}")
    return passed, report


def verify(result):
    passed, report = result
    lines = [(passed == len(CASES), f"requests passing: {passed} of {len(CASES)}")]
    lines += [(False, f"  {line}") for line in report[:3]]
    return lines
