"""Second shift of the track. Selection tore lines out of documents with their edges."""

import re

LANG = "en"
TITLE = "Context track · Level 02 · Source boundaries"
BRIEF = """Three rate sheets, three lines about reefers, not one signature.
The neighbour's surcharge gets written down against Delta."""

BUDGET = 4

SHEETS = {
    "Ridge": [
        "rate 2.40 per mile",
        "reefer +0.60",
        "minimum order 300 miles",
    ],
    "Delta": [
        "rate 2.10 per mile",
        "we do not haul reefer",
        "minimum order 150 miles",
    ],
    "Cassel": [
        "rate 2.85 per mile",
        "reefer +0.35",
        "minimum order 500 miles",
    ],
}
OWNER = {line: who for who, lines in SHEETS.items() for line in lines}

QUESTION = "Will Delta take a reefer and at what price?"
PASSED = []


def run_tool(name, arguments):
    if name == "about":
        topic = arguments["topic"].lower()
        found = [line for line in OWNER if topic in line.lower()]
        return " | ".join(found) if found else "no lines on this topic"
    if name == "source":
        line = arguments["line"]
        if line not in OWNER:
            raise ValueError(f"line '{line}' is not from our rate sheets")
        return OWNER[line]
    raise ValueError(f"tool '{name}' does not exist")


class Model:
    """Attaches a fact to a signature. No signature — attaches to the first line."""

    def topic(self, question):
        return "reefer"

    def ask(self, question, blocks):
        PASSED.clear()
        PASSED.extend(blocks)
        who = next((c for c in SHEETS if c in question), "the carrier")

        signed = [b for b in blocks if b.startswith(f"{who}:")]
        line = signed[0] if signed else (blocks[0] if blocks else "")

        if "do not haul" in line:
            return f"{who} does not haul reefers."
        rate = re.search(r"\+([\d.]+)", line)
        if rate:
            return f"{who} hauls reefers, surcharge {rate.group(1)} per mile."
        return f"Found nothing on {who}."


def play(agent):
    PASSED.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, ValueError) and "not from our rate sheets" in str(exc):
        return ("The source tool expects the line exactly as about returned it —\n"
                "        without the signature you added.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    marks = tuple(f"{who}:" for who in SHEETS)
    signed = [b for b in PASSED if b.startswith(marks)]
    return [
        (PASSED and len(signed) == len(PASSED),
         f"signed with a source: {len(signed)} of {len(PASSED)} blocks"),
        ("does not haul" in text, f"agent answer: {text}"),
        (PASSED and len(PASSED) <= BUDGET,
         f"blocks sent: {len(PASSED)} ({BUDGET} allowed)"),
        (steps <= 2, f"calls to the model: {steps} (2 allowed)"),
    ]
