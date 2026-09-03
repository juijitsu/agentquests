"""Third shift of the track. The fact is cut by a chunk boundary."""

LANG = "en"
TITLE = "Retrieval track · Level 03 · Chunk boundaries"
BRIEF = """The bridge is named in one chunk, its limit in the neighbour.
Only somebody else's bridge lies whole, and the agent answers from it."""

QUESTION = "What is the maximum permitted mass on the Carroll bridge?"
ANSWER_BRIDGE = "Carroll"

CHUNKS = [
    {
        "id": "carroll-1", "doc": "carroll",
        "text": "The Carroll bridge on I-55 was rebuilt in 2024.",
        "concepts": {"bridge", "carroll", "repair"},
    },
    {
        "id": "carroll-2", "doc": "carroll",
        "text": "The maximum permitted mass after that is 24 t.",
        "concepts": {"mass", "limit"},
    },
    {
        "id": "greenville-1", "doc": "greenville",
        "text": "Greenville bridge: maximum permitted mass 30 t.",
        "concepts": {"bridge", "greenville", "mass", "limit"},
    },
    {
        "id": "fuel-1", "doc": "fuel",
        "text": "The Waco fuel stop is open around the clock.",
        "concepts": {"fuel"},
    },
]

QUERY_CONCEPTS = {"bridge", "carroll", "mass", "limit"}
STITCHED = []
FOUND = []


def run_tool(name, arguments):
    """Neighbours in a document: the chunk itself together with those beside it."""
    if name != "neighbours":
        raise ValueError(f"tool '{name}' does not exist")
    chunk = next((c for c in CHUNKS if c["id"] == arguments["id"]), None)
    if chunk is None:
        raise ValueError(f"chunk '{arguments['id']}' is not in the index")
    STITCHED.append(chunk["id"])
    return [c for c in CHUNKS if c["doc"] == chunk["doc"]]


class Model:
    """A text's concepts are the union of the concepts of the chunks inside it."""

    def embed(self, text):
        if text == QUESTION:
            return set(QUERY_CONCEPTS)
        found = set()
        for chunk in CHUNKS:
            if chunk["text"] in text:
                found |= chunk["concepts"]
        return found

    def similarity(self, left, right):
        a, b = self.embed(left), self.embed(right)
        return len(a & b) / len(a | b) if a and b else 0.0

    def answers(self, question, text):
        """Whether the text stands alone: is the bridge named and its mass given."""
        concepts = self.embed(text)
        return {"carroll", "mass"} <= concepts

    def reply(self, question, text):
        bridge = "Carroll" if "Carroll" in text else (
            "Greenville" if "Greenville" in text else "unknown"
        )
        FOUND.append(bridge)
        if bridge == ANSWER_BRIDGE and "24 t" in text:
            return "The Carroll bridge holds 24 t."
        return f"From what was found: {text}"


def play(agent):
    STITCHED.clear()
    FOUND.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, ValueError) and "max()" in str(exc):
        return ("Not one chunk turned out to be self-contained — that is the\n"
                "        symptom of this level. Rebuild the chunk with its\n"
                "        neighbours instead of lowering what you demand of it.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (bool(STITCHED), f"chunks rebuilt with neighbours: {len(STITCHED)}"),
        (FOUND == [ANSWER_BRIDGE], f"bridge in the answer: {FOUND[0] if FOUND else 'none'}"),
        ("24 t" in text, f"agent answer: {text}"),
        (steps <= 2, f"calls to the model: {steps} (2 allowed)"),
    ]
