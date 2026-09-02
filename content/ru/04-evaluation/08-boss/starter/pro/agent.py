"""Уровень 08 · профессионал. Финал трека.

Контракт:
    run() -> tuple[str, int]

Доступно:
    CASES — у каждого случая id и kind
    RUNS, RUBRIC, BAR
    run_tool("answer", {"case": id, "run": n}) -> ответ на n-м прогоне
    run_tool("in_prompt", {"case": id}) -> лежит ли случай в промпте
    model.judge_own(answer) / model.judge_blind(rubric, answer)
    model.decide(by_kind, flaky) -> str

Отчёт засчитан, если судил независимый судья; утечка проверена по всем
случаям и исключена из счёта; каждый случай прогнан RUNS раз; доля
посчитана внутри видов; неустойчивые случаи названы.
"""

from scenario import CASES, RUBRIC, RUNS, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
