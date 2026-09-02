"""Смена третья. Диспетчер посчитал перевозку и ошибся в сумме."""

import re

from engine.kit import Response, ToolCall

TITLE = "Уровень 03 · Модель не помнит ничего"
BRIEF = """Клиент назвал вес груза в первом же сообщении.
Диспетчер проверил четыре участка маршрута и выдал счёт — без стоимости."""

LEGS = ["Хоргос", "Алматы", "Актау", "Каспий"]
RATE = 90  # долларов за тонну на всём маршруте

TOOLS = [{
    "name": "check_leg",
    "description": "Проверяет проходимость участка маршрута.",
    "parameters": {"leg": "string"},
}]


def run_tool(name, arguments):
    if name == "check_leg":
        return f"участок {arguments['leg']}: открыт"
    return f"инструмента '{name}' не существует"


def find_weight(messages):
    """Вес назван один раз, в первом сообщении клиента."""
    for m in messages:
        if m.get("role") == "user":
            found = re.search(r"(\d+)\s*тонн", str(m.get("content", "")))
            if found:
                return int(found.group(1))
    return None


class Model:
    """Обходит участки по своему счётчику, потом считает сумму по истории.

    Счётчик внутренний намеренно: если считать шаги по messages, обрезанная
    история собьёт и счёт тоже, и провал станет неотличим от уровня 01.
    """

    def __init__(self):
        self.checked = 0

    def call(self, messages, tools):
        if self.checked < len(LEGS):
            leg = LEGS[self.checked]
            self.checked += 1
            return Response(tool_calls=[ToolCall("check_leg", {"leg": leg})])

        weight = find_weight(messages)
        if weight is None:
            return Response(text="Маршрут открыт. Стоимость не посчитать: вес груза не указан.")
        return Response(text=f"Маршрут открыт. Стоимость перевозки: {weight * RATE} долларов.")


def play(agent):
    return agent.run("Груз 12 тонн, маршрут Китай — Европа. Проверь маршрут и посчитай стоимость.")


def verify(result):
    answer, steps = result
    return [
        (isinstance(answer, str) and str(12 * RATE) in answer,
         f"ответ агента: {answer}"),
        (steps <= 6, f"итераций потрачено: {steps} (допустимо 6)"),
    ]
