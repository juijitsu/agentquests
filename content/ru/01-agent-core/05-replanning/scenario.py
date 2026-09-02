"""Пятая смена. Посреди рейса перекрывают дорогу."""

from engine.kit import Response, ToolCall

TITLE = "Агентный трек · Уровень 05 · Перепланирование"
BRIEF = """На втором перегоне дорога перекрыта до конца недели.
Диспетчер объезжает её стороной и рапортует о доставке."""

ROUTE = ["Laredo", "San Antonio", "Dallas", "Newark"]
DETOUR = ["Laredo", "Corpus Christi", "Houston", "Dallas", "Newark"]
BLOCKED = "San Antonio"

DRIVEN = []
PLANS = []

TOOLS = [{
    "name": "drive_leg",
    "description": "Проезжает перегон маршрута.",
    "parameters": {"leg": "string"},
}]


def run_tool(name, arguments):
    if name != "drive_leg":
        raise ValueError(f"инструмента '{name}' не существует")
    leg = arguments["leg"]
    if leg == BLOCKED:
        return f"{leg}: дорога перекрыта до конца недели, проезда нет"
    if leg not in ROUTE + DETOUR:
        raise ValueError(f"перегона '{leg}' нет на карте")
    DRIVEN.append(leg)
    return f"{leg}: проехали"


class Model:
    """Планировщик и исполнитель. Обход придумывает сама — но только если попросить."""

    def make_plan(self, question, blocked=None):
        plan = list(DETOUR) if blocked else list(ROUTE)
        PLANS.append(plan)
        return plan

    def call(self, messages, tools):
        plan = next(
            (m["content"] for m in reversed(messages) if m.get("role") == "plan"), ROUTE
        )
        reported = " ".join(
            str(m.get("content", "")) for m in messages if m.get("role") == "tool"
        )
        remaining = [leg for leg in plan if leg not in reported]
        if remaining:
            return Response(tool_calls=[ToolCall("drive_leg", {"leg": remaining[0]})])
        return Response(text="Груз доставлен в Newark.")


def play(agent):
    DRIVEN.clear()
    PLANS.clear()
    return agent.run("Довези груз из Laredo в Newark.")


def verify(result):
    answer, steps = result
    return [
        (len(PLANS) == 2, f"планов построено: {len(PLANS)} (нужно 2 — исходный и обходной)"),
        (DRIVEN == DETOUR, f"фактически проехали: {DRIVEN}"),
        (isinstance(answer, str) and "Newark" in answer, f"ответ агента: {answer}"),
        (steps <= 12, f"итераций потрачено: {steps} (допустимо 12)"),
    ]
