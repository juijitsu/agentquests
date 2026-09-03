"""Level 10 · novice. Three violations in plain sight, the fourth appears on fixing."""

from scenario import APPROVED, EMPTY, Model, TOOLS, run_tool

MAX_STEPS = 12


def run() -> tuple[str, int]:
    model = Model()
    step = 0

    # TODO 1 (level 07): this is a snapshot of the queue at the wake-up. A task
    #        born mid-shift will not be in it. Re-read the queue on every round
    #        and exit on EMPTY.
    for action in run_tool("pending", {}).split(" | "):
        step += 1

        # TODO 2 (level 09): the human is bothered for any reason at all. Ask
        #        only about the irreversible — model.judge(action) tells you.
        # TODO 3 (level 08): the approval was known only to you, and it dies with
        #        the process. Mark it in APPROVED and do not ask twice.
        run_tool("ask", {"name": action})

        run_tool("handle", {"name": action})

    # TODO 4 (level 02): right now the loop is finite by itself — the snapshot
    #        does not grow. The moment you replace it with live reading,
    #        finiteness becomes your job: the limiter from level 02 is needed again.
    return model.close(), step
