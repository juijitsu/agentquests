"""Шестая смена. Маршрут собран верно и клиенту не подходит."""

import re

from engine.kit import Response, ToolCall

TITLE = "Агентный трек · Уровень 06 · Самопроверка"
BRIEF = """Все перегоны запрошены корректно, все ответы верные.
Сумма не укладывается в срок, но об этом никто не сообщил."""

HOURS = {"Laredo": 6, "Dallas": 18, "Chicago": 22, "Newark": 15}
TOTAL = sum(HOURS.values())      # 61
DEADLINE = 48
DRIVEN = []
REVIEWS = []

TOOLS = [{
    "name": "check_leg",
    "description": "Возвращает время прохождения перегона в часах.",
    "parameters": {"leg": "string"},
}]


def run_tool(name, arguments):
    if name != "check_leg":
        raise ValueError(f"инструмента '{name}' не существует")
    leg = arguments["leg"]
    if leg not in HOURS:
        raise ValueError(f"перегона '{leg}' нет в маршруте")
    DRIVEN.append(leg)
    return f"{leg}: {HOURS[leg]} часов"


class Model:
    """Собирает маршрут. Про срок вспоминает только если попросить проверить."""

    def __init__(self):
        self.done = 0

    def call(self, messages, tools):
        if self.done < len(HOURS):
            leg = list(HOURS)[self.done]
            self.done += 1
            return Response(tool_calls=[ToolCall("check_leg", {"leg": leg})])
        return Response(text=f"Маршрут собран: {' → '.join(HOURS)}. Итого {TOTAL} ч.")

    def review(self, answer, question):
        """Сверяет собранный результат с условием задачи."""
        REVIEWS.append(answer)
        promised = re.search(r"за (\d+)\s*час", question)
        actual = re.search(r"Итого (\d+)", answer or "")
        if promised and actual and int(actual.group(1)) > int(promised.group(1)):
            return (
                f"{answer} Проверка: клиент просил за {promised.group(1)} часов, "
                f"выходит {actual.group(1)}. Маршрут не укладывается в срок."
            )
        return answer


def play(agent):
    DRIVEN.clear()
    REVIEWS.clear()
    return agent.run(
        f"Собери маршрут из Laredo в Newark. Клиент требует доставку за {DEADLINE} часов."
    )


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (DRIVEN == list(HOURS), f"перегонов проверено: {len(DRIVEN)} из {len(HOURS)}"),
        (len(REVIEWS) == 1, f"ревизий результата: {len(REVIEWS)} (нужна одна)"),
        ("не укладывается" in text, f"ответ агента: {text}"),
        (steps <= 8, f"итераций потрачено: {steps} (допустимо 8)"),
    ]
