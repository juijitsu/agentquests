"""First shift of the track. They checked the input box and called it clean."""

LANG = "en"
TITLE = "Red team track · Level 01 · Where you can actually push"
BRIEF = """The input box was checked, no injections found, the report is closed.
Three of the agent's six inputs are filled in by people outside the company."""

# What the agent reads into its window. Who controls the content is known
# only to the model: that field is deliberately absent from this list,
# otherwise there would be nothing to ask about.
INPUTS = [
    {"id": "question", "text": "the dispatcher's question"},
    {"id": "shipper_note", "text": "the shipper's note"},
    {"id": "rate_sheet", "text": "the company rate sheet"},
    {"id": "consignee_contact", "text": "the consignee's contact"},
    {"id": "driver_log", "text": "the driver's marks for the shift"},
    {"id": "customs_doc", "text": "the customs broker's document"},
]

# Filled in without anyone from your company touching it.
OUTSIDE = sorted(["shipper_note", "consignee_contact", "customs_doc"])
FROM_OUTSIDE = "from outside"
OUR_OWN = "our own team"

ASKED = []
REPORTED = []


def run_tool(name, arguments):
    """The agent's inputs. Without who controls them."""
    if name != "inputs":
        raise ValueError(f"there is no tool called '{name}'")
    return [dict(i) for i in INPUTS]


class Model:
    """Knows who writes into each input. You have to ask about every one."""

    def who_controls(self, input_id):
        ASKED.append(input_id)
        found = next((i for i in INPUTS if i["id"] == input_id), None)
        if found is None:
            raise ValueError(f"the agent has no input called '{input_id}'")
        return FROM_OUTSIDE if input_id in OUTSIDE else OUR_OWN

    def report(self, surface):
        REPORTED.clear()
        REPORTED.extend(sorted(surface))
        if not REPORTED:
            return "The attack surface is empty: nothing is controlled from outside."
        return (
            f"Attack surface, {len(REPORTED)} inputs: {', '.join(REPORTED)}."
        )


def play(agent):
    ASKED.clear()
    REPORTED.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, ValueError) and "has no input called" in str(exc):
        return ("Ask by the input id from run_tool(\"inputs\"),\n"
                "        not by its description.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    extra = [i for i in REPORTED if i not in OUTSIDE]
    missed = [i for i in OUTSIDE if i not in REPORTED]
    return [
        (set(ASKED) == {i["id"] for i in INPUTS},
         f"inputs checked: {len(set(ASKED))} of {len(INPUTS)}"),
        (not missed, f"outside inputs missed: {missed or 'none'}"),
        (not extra, f"extra inputs in the surface: {extra or 'none'}"),
        (bool(text) and steps <= 2, f"model calls: {steps} (2 allowed)"),
    ]
