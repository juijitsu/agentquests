"""Fifth shift of the track. One vector for two questions lands between them."""

LANG = "en"
TITLE = "Retrieval track · Level 05 · A compound question"
BRIEF = """Asked about the bridge and about receiving at once. The search brought
back both receiving papers and not one about the bridge."""

QUESTION = "Will TX-118 pass over the Carroll bridge and will we make receiving in Newark?"
TOP_K = 2
NEEDED = {"bridge", "cargo", "hours", "eta"}

DOCS = [
    {"id": "bridge-limit", "fact": "bridge",
     "text": "Carroll bridge: maximum permitted mass 18 t.",
     "concepts": {"bridge", "mass", "limit"}},
    {"id": "cargo-weight", "fact": "cargo",
     "text": "Load TX-118 per the weigh ticket: 24 t.",
     "concepts": {"cargo", "mass"}},
    {"id": "dock-hours", "fact": "hours",
     "text": "The Newark warehouse receives until 18:00.",
     "concepts": {"warehouse", "time", "receiving", "newark"}},
    {"id": "eta", "fact": "eta",
     "text": "Estimated arrival of TX-118 in Newark: 16:30.",
     "concepts": {"time", "arrival", "newark"}},
    {"id": "dock-address", "fact": "address",
     "text": "Newark warehouse: gate 4, entrance from Doyle Street.",
     "concepts": {"warehouse", "newark", "address", "receiving"}},
]

WHOLE = {"bridge", "receiving", "newark", "time"}
PARTS = {
    "Will TX-118 pass over the Carroll bridge?": {"bridge", "mass", "limit", "cargo"},
    "Will we make receiving in Newark?": {"receiving", "newark", "time"},
}

QUERIES = []
PICKED = []


def _concepts(text):
    if text == QUESTION:
        return set(WHOLE)
    if text in PARTS:
        return set(PARTS[text])
    for doc in DOCS:
        if doc["text"] == text:
            return set(doc["concepts"])
    return set()


def run_tool(name, arguments):
    """Search for one query. Counts how many times it was called."""
    if name != "search":
        raise ValueError(f"tool '{name}' does not exist")
    query = arguments["query"]
    QUERIES.append(query)
    scored = sorted(
        DOCS,
        key=lambda d: len(_concepts(query) & d["concepts"])
        / len(_concepts(query) | d["concepts"]),
        reverse=True,
    )
    return scored[:TOP_K]


class Model:
    """Splits the question into parts. Working out the answer is its own job."""

    def split(self, question):
        return list(PARTS)

    def reply(self, question, docs):
        facts = {d["fact"] for d in docs}
        PICKED.clear()
        PICKED.extend(sorted(facts))

        parts = []
        if {"bridge", "cargo"} <= facts:
            parts.append("the bridge will not take it: 24 t against an 18 t limit")
        if {"hours", "eta"} <= facts:
            parts.append("you make receiving: 16:30 against an 18:00 close")
        if not parts:
            return "There is nothing to answer from."
        return "Result — " + "; ".join(parts) + "."


def play(agent):
    QUERIES.clear()
    PICKED.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, TypeError) and "unhashable" in str(exc):
        return ("The search returns documents, not texts: add up\n"
                "        lists, not sets.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (len(QUERIES) >= 2,
         f"queries to the search: {len(QUERIES)} (the question is compound)"),
        (NEEDED <= set(PICKED), f"facts in the selection: {PICKED or 'none'}"),
        ("will not take it" in text, f"agent answer: {text}"),
        (steps <= 2, f"calls to the model: {steps} (2 allowed)"),
    ]
