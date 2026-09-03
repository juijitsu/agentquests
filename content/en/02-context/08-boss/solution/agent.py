"""Level 08 · reference. Five duties inside one assembly."""

from scenario import BUDGET, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    blocks = run_tool("blocks", {})

    # 06: not by age and not by value, but by return per unit of cost.
    ranked = sorted(blocks, key=lambda b: model.worth(b) / b["cost"], reverse=True)

    brief = []
    spent = 0
    for block in ranked:
        if spent + block["cost"] > BUDGET:
            continue  # an expensive block does not end the pass: cheap ones follow
        # 02 and 07: the role says how to read it; the source says whom to call.
        # 05: nothing is collapsed, both weight readings travel as they are.
        brief.append({
            "role": "data",
            "id": block["id"],
            "source": block["source"],
            "text": block["text"],
            "cost": block["cost"],
        })
        spent += block["cost"]

    return model.ask(question, brief), 1
