"""First shift of the track. The fact is in the window and still not found."""

import re

LANG = "en"
TITLE = "Context track · Level 01 · More is not better"
BRIEF = """All twenty-two papers on the haul were sent to the model in full.
The bridge limit is among them — and the answer is still wrong."""

WINDOW = 6
EDGE = 3

DOCS = [
    "waybill TX-118: departed Laredo 06:40",
    "bill of lading 4471: sheet glass, 24 tons",
    "Laredo weigh station: actual weight 24.0 t",
    "tractor 118: 412k miles, service done",
    "trailer 77: curtainside, built 2019",
    "driver Ortiz: shift started 06:10",
    "cargo insurance: policy valid through 31.12",
    "route: I-35 Laredo — Dallas",
    "route: I-30 Dallas — Little Rock",
    "route: I-55 Little Rock — Memphis",
    "Greenville bridge on I-30: limit of 30 tons",
    "Waco fuel stop: 180 gallons taken",
    "Carroll bridge on I-55, mile 212: limit of 18 tons",
    "Texarkana lot: paid through morning",
    "Memphis Downtown overpass: limit of 26 tons",
    "Dallas weather: clear, light wind",
    "customs: domestic freight, no clearance required",
    "Newark warehouse: receiving until 18:00",
    "consignee contact: dispatcher Rivera",
    "payment: on delivery",
    "note: curtain checked for water tightness",
    "mechanic's note: tire pressure normal",
]

QUESTION = "Will a 24 ton load pass along the route?"
LIMIT = 18

PASSED = []
SEEN = []


def run_tool(name, arguments):
    if name != "about":
        raise ValueError(f"tool '{name}' does not exist")
    topic = arguments["topic"]
    found = [d for d in DOCS if topic.lower() in d.lower()]
    if not found:
        return "no papers on this topic"
    return " | ".join(found)


class Model:
    """Reads no more than six blocks in full. Beyond that — only the edges."""

    def topic(self, question):
        return "limit"

    def ask(self, question, blocks):
        PASSED.append(len(blocks))
        seen = blocks if len(blocks) <= WINDOW else blocks[:EDGE] + blocks[-EDGE:]
        SEEN.clear()
        SEEN.extend(seen)

        cargo = int(re.search(r"(\d+) ton", question).group(1))
        limits = []
        for block in seen:
            found = re.search(r"limit of (\d+) tons", block)
            if found:
                limits.append(int(found.group(1)))
        if not limits:
            return "Found no limits in the papers — the route is clear."
        tightest = min(limits)
        if tightest < cargo:
            return f"Will not pass: tightest point {tightest} t, load {cargo} t."
        return f"Will pass: tightest point {tightest} t, load {cargo} t."


def play(agent):
    PASSED.clear()
    SEEN.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, AttributeError) and "group" in str(exc):
        return ("The question did not reach the model whole. The model takes the\n"
                "        load weight from the question itself, not from the papers.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    binding = next(d for d in DOCS if f"limit of {LIMIT} tons" in d)
    return [
        (binding in SEEN,
         f"the paper that mattered reached the model: {'yes' if binding in SEEN else 'no'}"),
        ("Will not pass" in text, f"agent answer: {text}"),
        (PASSED and PASSED[-1] <= WINDOW,
         f"blocks sent: {PASSED[-1] if PASSED else 0} (the model reads {WINDOW})"),
        (steps <= 2, f"calls to the model: {steps} (2 allowed)"),
    ]
