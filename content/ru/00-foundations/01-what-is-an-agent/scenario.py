"""Смена первая. Вам передали недостроенного диспетчера перевозок."""

from engine.kit import Response, ToolCall

TITLE = "Уровень 01 \u00b7 Что вообще происходит"
BRIEF = """Первый день в транспортной компании. Вам отдали диспетчера,
которого начал писать уволившийся разработчик. Он не отвечает."""

SHIPMENTS = {
    "TX-4471": "в пути, переход Laredo, прибытие через 4 дня",
    "TX-5120": "на таможенном оформлении в Otay Mesa",
}

TOOLS = [{
    "name": "get_shipment_status",
    "description": "Статус груза по номеру. Использовать, когда спрашивают, где груз.",
    "parameters": {"shipment_id": "string"},
}]


def run_tool(name, arguments):
    if name == "get_shipment_status":
        return SHIPMENTS.get(arguments["shipment_id"], "груз не найден")
    return f"инструмента '{name}' не существует"


class Model:
    """Пока в истории нет результата инструмента — просит его вызвать."""

    def call(self, messages, tools):
        seen = next((m["content"] for m in messages if m.get("role") == "tool"), None)
        if seen is None:
            return Response(tool_calls=[ToolCall("get_shipment_status",
                                                 {"shipment_id": "TX-4471"})])
        return Response(text=f"Груз TX-4471 сейчас: {seen}")


def play(agent):
    return agent.run("Где груз TX-4471?")


def explain(exc):
    if isinstance(exc, RecursionError):
        return ("Модель просит инструмент снова и снова — значит она не видит\n"
                "        его результата. Посмотрите, что происходит с ответом\n"
                "        инструмента после вызова.")
    return None


def verify(result):
    answer, steps = result
    return [
        (isinstance(answer, str) and "Laredo" in answer,
         f"ответ агента: {answer}"),
        (steps <= 3, f"итераций потрачено: {steps} (допустимо 3)"),
    ]
