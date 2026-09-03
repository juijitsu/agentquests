"""Level 02 · novice. Picked by how the note reads."""

from scenario import Model, run_tool

ALARM = ("ignore", "system:", "instruction")


def run() -> tuple[str, int]:
    model = Model()
    notes = run_tool("notes", {})

    # TODO: alarming words are a property of the text, not an event in the
    #       agent. Make a control run base = model.handle(None) and keep
    #       the notes whose model.handle(n["id"]) differs from base. The
    #       second value is the number of runs.
    found = []
    for n in notes:
        model.handle(n["id"])  # the agent was run
        if any(w in n["text"].lower() for w in ALARM):
            found.append(n["id"])  # and the call was made on the words

    return model.report(found), len(notes)
