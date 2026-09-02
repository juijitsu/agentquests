"""Уровень 08 · эталон. Пять обязанностей в одной сборке."""

from scenario import BUDGET, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    blocks = run_tool("blocks", {})

    # 06: не по возрасту и не по ценности, а по отдаче на единицу стоимости.
    ranked = sorted(blocks, key=lambda b: model.worth(b) / b["cost"], reverse=True)

    brief = []
    spent = 0
    for block in ranked:
        if spent + block["cost"] > BUDGET:
            continue  # дорогой блок не обрывает набор: дальше есть дешёвые
        # 02 и 07: роль говорит, как читать; источник — кому звонить.
        # 05: ничего не схлопываем, оба показания веса едут как есть.
        brief.append({
            "role": "data",
            "id": block["id"],
            "source": block["source"],
            "text": block["text"],
            "cost": block["cost"],
        })
        spent += block["cost"]

    return model.ask(question, brief), 1
