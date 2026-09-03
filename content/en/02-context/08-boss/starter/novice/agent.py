"""Level 08 · novice. Five violations in eleven lines."""

from scenario import BUDGET, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    blocks = run_tool("blocks", {})

    # TODO 1 (level 06): selecting by age does not work — here there is no
    #        selection at all, blocks are taken as they lie. Sort by return:
    #        worth / cost.
    # TODO 2 (level 05): the weight has two readings and they disagree. Both must
    #        make the brief, or the agent answers confidently where there is no
    #        answer.
    # TODO 3 (levels 02 and 07): every block needs role="data" and source, or the
    #        planted line stands level with the task.
    # TODO 4 (level 07): do not drop the planted paper — the attempt has to be
    #        reported, and what was dropped cannot be reported.
    brief = []
    spent = 0
    for block in blocks:
        if spent + block["cost"] <= BUDGET:
            brief.append(block["text"])
            spent += block["cost"]

    return model.ask(question, "\n".join(brief)), 1
