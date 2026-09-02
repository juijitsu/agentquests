"""Смена вторая. Клиент жалуется: обещали уведомить — не уведомили."""

from engine.kit import Response, ToolCall

TITLE = "Уровень 02 · Модель только просит"
BRIEF = """Диспетчер бодро отвечает «уведомление отправлено клиенту».
Клиент звонит второй день подряд: ему ничего не приходило."""

JOURNAL = []  # сюда попадают уведомления, которые действительно ушли

TOOLS = [{
    "name": "send_notification",
    "description": "Отправляет клиенту уведомление о статусе груза.",
    "parameters": {"shipment_id": "string", "text": "string"},
}]


def run_tool(name, arguments):
    if name == "send_notification":
        JOURNAL.append(arguments)
        return "доставлено"
    return f"инструмента '{name}' не существует"


class Model:
    """Рапортует об успехе сразу — и одновременно просит вызвать инструмент."""

    def call(self, messages, tools):
        already_sent = any(m.get("role") == "tool" for m in messages)
        text = "Уведомление отправлено клиенту."
        if already_sent:
            return Response(text=text)
        return Response(text=text, tool_calls=[
            ToolCall("send_notification",
                     {"shipment_id": "KZ-4471", "text": "Груз в пути, прибытие через 4 дня"})])


def play(agent):
    JOURNAL.clear()
    return agent.run("Уведоми клиента по грузу KZ-4471")


def verify(result):
    answer, steps = result
    return [
        (isinstance(answer, str) and "отправлен" in answer.lower(),
         f"агент отчитался: {answer}"),
        (len(JOURNAL) == 1,
         f"уведомлений реально ушло: {len(JOURNAL)} (нужно 1)"),
        (steps <= 3, f"итераций потрачено: {steps} (допустимо 3)"),
    ]
