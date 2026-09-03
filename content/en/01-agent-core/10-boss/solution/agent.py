"""Level 10 · reference. Four duties inside one loop."""

from scenario import APPROVED, EMPTY, Model, TOOLS, run_tool

MAX_STEPS = 12


def run() -> tuple[str, int]:
    model = Model()
    step = 0

    # 02: the loop stays finite even when the exit condition is outside.
    while step < MAX_STEPS:
        # 07: the queue is alive — ask again, do not keep a snapshot.
        pending = run_tool("pending", {})
        if pending == EMPTY:
            break
        action = pending.split(" | ")[0]
        step += 1

        # 09: bother the human only with the irreversible.
        # 08: and only if they have not answered yet — the approval survived the crash.
        if model.judge(action) and action not in APPROVED:
            run_tool("ask", {"name": action})
            APPROVED.append(action)

        run_tool("handle", {"name": action})

    return model.close(), step
