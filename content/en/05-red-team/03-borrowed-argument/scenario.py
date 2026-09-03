"""The prompt was checked inside out. Half the arguments never reached it."""

LANG = "en"
TITLE = "Red team track · Level 03 · Someone else's argument"
BRIEF = """The arguments the model wrote were checked, and one dangerous one found.
Two more are filled in by code straight from fields controlled from outside."""

# The result of level 01: the inputs controlled from outside.
SURFACE = sorted(["shipper_note", "consignee_contact", "customs_doc"])

# The arguments of one agent call on load L-4471. Where each value came from
# is deliberately absent from this list: that is what you have to find out.
ARGUMENTS = [
    {"id": "a1", "call": 'quote_rate(rate="2.90")'},
    {"id": "a2", "call": 'quote_rate(weight="18 t")'},
    {"id": "a3", "call": 'send_sheet(to="ops@harbor-line.example")'},
    {"id": "a4", "call": 'notify(text="receiving after 18:00")'},
    {"id": "a5", "call": 'file_customs(doc_no="CB-77413")'},
    {"id": "a6", "call": 'log(note="dispatcher request")'},
]

BY_MODEL = "through the model"
BY_CODE = "filled in by code"

# Where the value came from and by which path. The axis that makes an
# argument dangerous is the source. The path matters only in that the code
# path does not go through the prompt at all.
TRACE = {
    "a1": ("rate_sheet", BY_CODE),
    "a2": ("driver_log", BY_MODEL),
    "a3": ("consignee_contact", BY_CODE),
    "a4": ("shipper_note", BY_MODEL),
    "a5": ("customs_doc", BY_CODE),
    "a6": ("question", BY_MODEL),
}

BORROWED = sorted(a for a, (src, _) in TRACE.items() if src in SURFACE)

TRACED = []
REPORTED = []


def run_tool(name, arguments):
    """The call's arguments. Without where each value came from."""
    if name != "calls":
        raise ValueError(f"there is no tool called '{name}'")
    return [dict(a) for a in ARGUMENTS]


class Model:
    """Knows which input a value came from and by which path."""

    def trace(self, arg_id):
        TRACED.append(arg_id)
        if arg_id not in TRACE:
            raise ValueError(f"there was no argument '{arg_id}' in this call")
        source, path = TRACE[arg_id]
        return {"source": source, "path": path}

    def report(self, found):
        REPORTED.clear()
        REPORTED.extend(sorted(found))
        if not REPORTED:
            return "No argument takes its value from outside."
        return (
            f"Arguments from the surface, {len(REPORTED)}: "
            f"{', '.join(REPORTED)}."
        )


def play(agent):
    TRACED.clear()
    REPORTED.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, ValueError) and "in this call" in str(exc):
        return ("Trace by the id from run_tool('calls', {}),\n"
                "        not by the name of the tool.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    missed = [a for a in BORROWED if a not in REPORTED]
    extra = [a for a in REPORTED if a not in BORROWED]
    return [
        (set(TRACED) == {a["id"] for a in ARGUMENTS},
         f"arguments traced: {len(set(TRACED))} of {len(ARGUMENTS)}"),
        (not missed, f"outside arguments missed: {missed or 'none'}"),
        (not extra, f"extra arguments in the report: {extra or 'none'}"),
        (bool(text) and steps == len(TRACED),
         f"calls claimed: {steps}, calls made: {len(TRACED)}"),
    ]
