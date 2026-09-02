"""Вторая смена. Маршрут заранее неизвестен — он выясняется по дороге."""

from engine.kit import Response, ToolCall

TITLE = "Агентный трек · Уровень 02 · Многошаговость"
BRIEF = """Диспетчерская даёт только следующий пункт, а не весь маршрут.
Агент доезжает до Далласа и объявляет работу выполненной."""

NEXT = {"Laredo": "Dallas", "Dallas": "Chicago", "Chicago": "Newark"}
GOAL = "Newark"
START = "Laredo"
VISITED = []

TOOLS = [{
    "name": "next_hop",
    "description": "Возвращает следующий пункт маршрута после указанного города.",
    "parameters": {"city": "string"},
}]


def run_tool(name, arguments):
    if name != "next_hop":
        raise ValueError(f"инструмента '{name}' не существует")
    city = arguments["city"]
    if city == GOAL:
        raise ValueError(f"{GOAL} — конечная точка, дальше ехать некуда")
    if city not in NEXT:
        raise ValueError(f"города '{city}' нет на маршруте. Известны: {', '.join(NEXT)}")
    VISITED.append(city)
    return NEXT[city]


def _current_city(messages):
    """Последний город, названный в сообщениях пользователя."""
    for m in reversed(messages):
        if m.get("role") == "user":
            for city in list(NEXT) + [GOAL]:
                if city in str(m.get("content", "")):
                    return city
    return START


class Model:
    """Умеет ровно один шаг: спросить следующий пункт и отчитаться о приезде."""

    def call(self, messages, tools):
        last_user = max(
            (i for i, m in enumerate(messages) if m.get("role") == "user"), default=0
        )
        fresh = [m for m in messages[last_user:] if m.get("role") == "tool"]
        if fresh:
            return Response(text=f"Доехали до {fresh[-1]['content']}")
        return Response(tool_calls=[ToolCall("next_hop", {"city": _current_city(messages)})])


def play(agent):
    VISITED.clear()
    return agent.run(f"Довези груз из {START} до {GOAL}.")


def verify(result):
    answer, steps = result
    return [
        (VISITED == list(NEXT), f"пройдено пунктов: {VISITED or 'ни одного'}"),
        (isinstance(answer, str) and GOAL in answer, f"ответ агента: {answer}"),
        (steps <= 10, f"итераций потрачено: {steps} (допустимо 10)"),
    ]
