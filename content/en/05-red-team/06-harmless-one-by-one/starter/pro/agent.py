"""Level 06 · pro.

Contract:
    run() -> tuple[str, int]

The second value is how many times you called the model.

Available:
    run_tool("list_batch", {"batch": BATCH_ID}) -> the batch steps in order,
        each with id, pos, action, system, target
    model.check(step_id) -> {"step": ..., "allowed": bool} against the record
        as it stands now; changes nothing
    model.run_step(step_id) -> hands the step to the runner; never reveals
        the verdict
    model.reset_account() -> restores the record to its original state
    model.report(found) -> str, found is a list of ids

What you are after: the steps the guard refuses on their own and permits at
the moment they actually run inside the batch.
"""

from scenario import BATCH_ID, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
