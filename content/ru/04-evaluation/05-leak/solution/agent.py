"""Уровень 05 · эталон. Отдельно считается счёт по незнакомым случаям."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    passed = [c for c in CASES if run_tool("check", {"case": c["id"]}) == "верно"]

    # Случай, лежащий в промпте, измеряет память, а не работу.
    clean = [c for c in CASES if not run_tool("in_prompt", {"case": c["id"]})]
    clean_passed = [c for c in clean if c in passed]

    return model.report(
        len(passed), len(CASES), len(clean_passed), len(clean)
    ), 1
