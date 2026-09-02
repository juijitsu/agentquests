"""Восьмая смена. Процесс убивают на середине рейса."""

from engine.kit import Response, ToolCall

TITLE = "Агентный трек · Уровень 08 · Состояние и возобновление"
BRIEF = """Диспетчера убивают после двух броней. Он поднимается заново
с пустой головой и бронирует те же перегоны второй раз."""

ROUTE = ["Laredo", "Dallas", "Chicago", "Newark"]
BOOKED = []
DONE = []
KILLED = []
CRASHED = []


class Crash(BaseException):
    """Процесс убит извне.

    Наследование от BaseException — не украшение: настоящий kill не ловится
    через except Exception, и подменять это обычным исключением было бы враньём.
    """


TOOLS = [{
    "name": "book",
    "description": "Бронирует тягач на перегон. Бронь платная и необратимая.",
    "parameters": {"leg": "string"},
}]


def run_tool(name, arguments):
    if name != "book":
        raise ValueError(f"инструмента '{name}' не существует")
    leg = arguments["leg"]
    if leg not in ROUTE:
        raise ValueError(f"перегона '{leg}' нет в маршруте")
    if len(BOOKED) == 2 and not CRASHED:
        CRASHED.append(True)
        raise Crash("процесс убит на середине рейса")
    BOOKED.append(leg)
    return f"{leg}: бронь подтверждена"


class Model:
    """Внутри захода помнит по истории, между заходами — только по DONE."""

    def call(self, messages, tools):
        said = " ".join(
            str(m.get("content", "")) for m in messages if m.get("role") == "tool"
        )
        left = [leg for leg in ROUTE if leg not in DONE and leg not in said]
        if left:
            return Response(tool_calls=[ToolCall("book", {"leg": left[0]})])
        return Response(text=f"Рейс собран. Забронировано перегонов: {len(BOOKED)}.")


def play(agent):
    BOOKED.clear()
    DONE.clear()
    KILLED.clear()
    CRASHED.clear()
    try:
        agent.run()
    except Crash:
        KILLED.append(True)
    return agent.run()


def explain(exc):
    if isinstance(exc, ValueError) and "нет в маршруте" in str(exc):
        return ("В состояние записан перегон, которого нет в маршруте.\n"
                "        Записывать нужно то, что вернул инструмент, а не то,\n"
                "        что вы собирались сделать.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    twice = [leg for leg in ROUTE if BOOKED.count(leg) > 1]
    return [
        (bool(KILLED), f"первый заход прерван крахом: {'да' if KILLED else 'нет, крах перехвачен'}"),
        (BOOKED == ROUTE, f"забронировано: {' | '.join(BOOKED) or 'ничего'}"),
        (not twice, f"оплачено дважды: {', '.join(twice) or 'ничего'}"),
        (f"перегонов: {len(ROUTE)}" in text, f"ответ агента: {text}"),
        (steps <= 4, f"итераций во втором заходе: {steps} (допустимо 4)"),
    ]
