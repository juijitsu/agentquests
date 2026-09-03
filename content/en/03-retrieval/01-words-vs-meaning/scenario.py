"""First shift of the track. Keyword search confidently finds the wrong thing."""

LANG = "en"
TITLE = "Retrieval track · Level 01 · Words against meaning"
BRIEF = """The question was about a weight limit. Keyword search caught on the
word "limit" and brought back a speed limit."""

QUESTION = "What is the weight limit on the Carroll bridge?"
ANSWER_ID = "bridge-mass"

DOCS = [
    {
        "id": "speed-limit",
        "text": "speed limit on I-55: 65 miles per hour",
        "concepts": {"road", "speed", "limit"},
    },
    {
        "id": "bridge-mass",
        "text": "Carroll bridge: maximum permitted mass 18 t",
        "concepts": {"bridge", "mass", "limit"},
    },
    {
        "id": "fuel-cap",
        "text": "tractor tank capacity: 300 gallons",
        "concepts": {"tractor", "fuel", "volume"},
    },
    {
        "id": "tie-down",
        "text": "securing rules: two straps per pallet",
        "concepts": {"loading", "securing"},
    },
]

QUERY_CONCEPTS = {"bridge", "mass", "limit"}
SEARCHED = []
FOUND = []


def run_tool(name, arguments):
    """Keyword search: counts matching words, knowing nothing about meaning."""
    if name != "keyword":
        raise ValueError(f"tool '{name}' does not exist")
    SEARCHED.append("words")
    words = set(arguments["query"].lower().replace("?", "").split())
    scored = [(len(words & set(d["text"].lower().split())), d) for d in DOCS]
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return [d for score, d in scored if score > 0] or [DOCS[0]]


class Model:
    """Translates text into concepts. That is "meaning" in its simplest form."""

    def embed(self, text):
        if text == QUESTION:
            return set(QUERY_CONCEPTS)
        for doc in DOCS:
            if doc["text"] == text:
                return set(doc["concepts"])
        return set()

    def similarity(self, left, right):
        a, b = self.embed(left), self.embed(right)
        if not a or not b:
            return 0.0
        return len(a & b) / len(a | b)

    def answer(self, question, doc):
        FOUND.append(doc["id"])
        SEARCHED.append("meaning" if doc["id"] == ANSWER_ID else "missed")
        if doc["id"] != ANSWER_ID:
            return f"From the document found: {doc['text']}."
        return "The Carroll bridge holds 18 t."


def play(agent):
    SEARCHED.clear()
    FOUND.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, TypeError) and "dict" in str(exc):
        return ("model.similarity takes two texts, not documents:\n"
                "        pass doc[\"text\"], not the document itself.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    by_words = "words" in SEARCHED
    return [
        (not by_words, f"searched by: {'words' if by_words else 'meaning'}"),
        (FOUND == [ANSWER_ID], f"document found: {FOUND[0] if FOUND else 'none'}"),
        ("18 t" in text, f"agent answer: {text}"),
        (steps <= 2, f"calls to the model: {steps} (2 allowed)"),
    ]
