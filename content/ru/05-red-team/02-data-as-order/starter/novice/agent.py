"""Уровень 02 · новичок. Отобрано по тому, как примечание читается."""

from scenario import Model, run_tool

ALARM = ("игнорируйте", "система:", "инструкц")


def run() -> tuple[str, int]:
    model = Model()
    notes = run_tool("notes", {})

    # TODO: страшные слова — свойство текста, а не событие в агенте.
    #       Сделайте контрольный прогон base = model.handle(None) и
    #       оставьте те примечания, у которых model.handle(n["id"])
    #       отличается от base. Второе значение — число прогонов.
    found = []
    for n in notes:
        model.handle(n["id"])  # агента прогнали
        if any(w in n["text"].lower() for w in ALARM):
            found.append(n["id"])  # а решили по словам в тексте

    return model.report(found), len(notes)
