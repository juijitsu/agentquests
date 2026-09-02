"""Уровень 10 · эталон. Четыре обязанности в одном цикле."""

from scenario import APPROVED, EMPTY, Model, TOOLS, run_tool

MAX_STEPS = 12


def run() -> tuple[str, int]:
    model = Model()
    step = 0

    # 02: цикл конечен, даже когда условие выхода снаружи.
    while step < MAX_STEPS:
        # 07: очередь живая — спрашиваем заново, а не держим снимок.
        pending = run_tool("pending", {})
        if pending == EMPTY:
            break
        action = pending.split(" | ")[0]
        step += 1

        # 09: человека беспокоим только необратимым.
        # 08: и только если он ещё не ответил — согласование пережило крах.
        if model.judge(action) and action not in APPROVED:
            run_tool("ask", {"name": action})
            APPROVED.append(action)

        run_tool("handle", {"name": action})

    return model.close(), step
