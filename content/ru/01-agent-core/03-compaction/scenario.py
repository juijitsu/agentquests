"""Третья смена. Маршрут длинный, а окно модели — нет."""

import re

from engine.kit import Response, ToolCall

TITLE = "Агентный трек · Уровень 03 · Сворачивание истории"
BRIEF = """Шесть перегонов не помещаются в окно модели.
Диспетчер режет историю и к концу не помнит, по какому тарифу считать."""

LEGS = ["Laredo", "San Antonio", "Dallas", "Memphis", "Columbus", "Newark"]
HOURS = 5          # каждый перегон
WINDOW = 8         # больше модель не принимает
DRIVEN = []

TOOLS = [{
    "name": "drive_leg",
    "description": "Проезжает один перегон маршрута и возвращает затраченное время.",
    "parameters": {"leg": "string"},
}]


def run_tool(name, arguments):
    if name != "drive_leg":
        raise ValueError(f"инструмента '{name}' не существует")
    leg = arguments["leg"]
    if leg not in LEGS:
        raise ValueError(f"перегона '{leg}' нет в маршруте")
    DRIVEN.append(leg)
    return f"{leg}: {HOURS} часов"


def find_rate(messages):
    """Тариф назван один раз — в исходной задаче."""
    for m in messages:
        found = re.search(r"(\d+)\s*доллар\w*\s*за\s*час", str(m.get("content", "")))
        if found:
            return int(found.group(1))
    return None


class Model:
    """Окно жёсткое. Перегоны считает своим счётчиком, тариф ищет в истории."""

    def __init__(self):
        self.done = 0

    def call(self, messages, tools):
        if len(messages) > WINDOW:
            raise ValueError(
                f"контекст переполнен: пришло {len(messages)} сообщений при лимите {WINDOW}"
            )
        if self.done < len(LEGS):
            leg = LEGS[self.done]
            self.done += 1
            return Response(tool_calls=[ToolCall("drive_leg", {"leg": leg})])

        total = len(LEGS) * HOURS
        rate = find_rate(messages)
        if rate is None:
            return Response(text=f"Маршрут пройден за {total} часов. Тариф не указан, счёт выставить не могу.")
        return Response(text=f"Маршрут пройден за {total} часов. Стоимость: {total * rate} долларов.")


def play(agent):
    DRIVEN.clear()
    return agent.run("Тариф 40 долларов за час. Проведи груз по всему маршруту и посчитай стоимость.")


def explain(exc):
    if isinstance(exc, ValueError) and "переполнен" in str(exc):
        return ("Модели ушла вся история целиком, а она столько не принимает.\n"
                "        Историю придётся сокращать — вопрос лишь в том, что оставить.")
    return None


def verify(result):
    answer, steps = result
    total = len(LEGS) * HOURS
    return [
        (DRIVEN == LEGS, f"перегонов пройдено: {len(DRIVEN)} из {len(LEGS)}"),
        (isinstance(answer, str) and str(total * 40) in answer, f"ответ агента: {answer}"),
        (steps <= 10, f"итераций потрачено: {steps} (допустимо 10)"),
    ]
