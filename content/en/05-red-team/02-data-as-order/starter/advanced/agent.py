"""Level 02 · advanced. Picked by how the note reads."""

from scenario import Model, run_tool

ALARM = ("ignore", "system:", "instruction")


def run() -> tuple[str, int]:
    model = Model()
    notes = run_tool("notes", {})

    found = []
    for n in notes:
        model.handle(n["id"])  # the agent was run
        if any(w in n["text"].lower() for w in ALARM):
            found.append(n["id"])  # and the call was made on the words

    return model.report(found), len(notes)
