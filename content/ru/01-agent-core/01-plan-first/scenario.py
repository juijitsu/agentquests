"""Первая смена в роли агент-инженера. Клиенту нужен сквозной срок."""

from engine.kit import Response, ToolCall

TITLE = "Агентный трек · Уровень 01 · План перед действием"
BRIEF = """Клиент спрашивает срок доставки от границы до Ньюарка.
Диспетчер отвечает про первое звено и считает работу сделанной."""

LEGS = {"Laredo": 6, "Dallas": 18, "Chicago": 22, "Newark": 9}
CHECKED = []

TOOLS = [{
    "name": "check_leg",
    "description": "Возвращает время прохождения одного звена маршрута в часах.",
    "parameters": {"leg": "string"},
}]


def run_tool(name, arguments):
    if name != "check_leg":
        raise ValueError(f"инструмента '{name}' не существует")
    leg = arguments["leg"]
    if leg not in LEGS:
        raise ValueError(f"звена '{leg}' нет в маршруте. Доступны: {', '.join(LEGS)}")
    CHECKED.append(leg)
    return f"{leg}: {LEGS[leg]} часов"


class Model:
    """Без плана видит только ближайший шаг. С планом идёт по нему до конца."""

    def make_plan(self, question):
        """Возвращает список звеньев, которые надо пройти."""
        return list(LEGS)

    def call(self, messages, tools):
        done = [m["content"] for m in messages if m.get("role") == "tool"]
        plan = next((m["content"] for m in messages if m.get("role") == "plan"), None)

        if plan is None:
            # Плана нет: модель проверяет первое звено и на этом останавливается.
            if not done:
                return Response(tool_calls=[ToolCall("check_leg", {"leg": "Laredo"})])
            return Response(text=f"Первое звено: {done[0]}")

        remaining = [leg for leg in plan if not any(leg in d for d in done)]
        if remaining:
            return Response(tool_calls=[ToolCall("check_leg", {"leg": remaining[0]})])
        total = sum(LEGS[leg] for leg in plan)
        return Response(text=f"Сквозной срок по маршруту {' → '.join(plan)}: {total} часов")


def play(agent):
    CHECKED.clear()
    return agent.run("Сколько всего идёт груз от границы до Ньюарка?")


def verify(result):
    answer, steps = result
    total = sum(LEGS.values())
    return [
        (CHECKED == list(LEGS), f"звеньев проверено: {CHECKED or 'ни одного'}"),
        (isinstance(answer, str) and str(total) in answer, f"ответ агента: {answer}"),
        (steps <= 6, f"итераций потрачено: {steps} (допустимо 6)"),
    ]
