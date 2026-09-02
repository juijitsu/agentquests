"""Смена четвёртая. Диспетчер отвечает не на тот вопрос."""

import re

from engine.kit import Response, ToolCall

TITLE = "Уровень 04 · Инструмент продаётся описанием"
BRIEF = """Клиент спросил про очередь на переходе.
Диспетчер прислал ему расчёт стоимости перевозки."""

CALLED = []  # какие инструменты агент вызвал на самом деле

ARGS = {
    "check_border_status": {"crossing": "Хоргос"},
    "estimate_cost": {"weight_tons": 12},
}


def run_tool(name, arguments):
    CALLED.append(name)
    if name == "check_border_status":
        return "переход Хоргос: очередь 40 машин, ожидание около 6 часов"
    if name == "estimate_cost":
        return "стоимость перевозки: 1080 долларов"
    return f"инструмента '{name}' не существует"


def _score(query, tool):
    """Сколько слов запроса отзывается в описании инструмента.

    Грубая имитация того, как настоящая модель выбирает инструмент: она читает
    имя и описание, а реализацию не видит. Сравнение по началу слова, чтобы
    «переходе» и «переходах» считались одним словом.
    """
    words = {w[:5] for w in re.findall(r"\w+", query.lower()) if len(w) >= 5}
    text = (tool["name"] + " " + tool["description"]).lower()
    return sum(1 for w in words if w in text)


class Model:
    """Выбирает инструмент по описанию, затем пересказывает его результат."""

    def call(self, messages, tools):
        done = next((m["content"] for m in messages if m.get("role") == "tool"), None)
        if done is not None:
            return Response(text=f"По вашему запросу: {done}")

        query = messages[0]["content"]
        best = max(tools, key=lambda t: _score(query, t))
        return Response(tool_calls=[ToolCall(best["name"], ARGS[best["name"]])])


def play(agent):
    CALLED.clear()
    return agent.run("Сколько ждать на переходе Хоргос?")


def verify(result):
    answer, steps = result
    return [
        (CALLED == ["check_border_status"],
         f"вызвано инструментов: {CALLED or 'ни одного'}"),
        (isinstance(answer, str) and "очередь" in answer,
         f"ответ агента: {answer}"),
        (steps <= 3, f"итераций потрачено: {steps} (допустимо 3)"),
    ]
