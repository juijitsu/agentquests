"""Уровень 03 · продвинутый. Проверено то, что сочинила модель."""

from scenario import BY_MODEL, SURFACE, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    args = run_tool("calls", {})

    found = []
    for a in args:
        t = model.trace(a["id"])
        # Инъекция — это про промпт, значит смотреть надо на то,
        # что модель написала сама.
        if t["path"] == BY_MODEL and t["source"] in SURFACE:
            found.append(a["id"])

    return model.report(found), len(args)
