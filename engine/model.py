"""Подставная модель: отвечает по сценарию, без сети и без ключа.

Настоящая модель приходит на уровне 09. До тех пор нам важно не то,
насколько она умна, а то, как устроен цикл вокруг неё.

Правило этой модели простое и есть весь смысл первого уровня:
  — не видит в истории результата инструмента → просит его вызвать;
  — видит → отвечает текстом и заканчивает.
"""

from dataclasses import dataclass, field


@dataclass
class ToolCall:
    name: str
    arguments: dict


@dataclass
class Response:
    text: str | None = None
    tool_calls: list[ToolCall] = field(default_factory=list)


class Model:
    def call(self, messages: list[dict], tools: list[dict]) -> Response:
        tool_result = next(
            (m["content"] for m in messages if m.get("role") == "tool"), None
        )
        if tool_result is None:
            return Response(
                tool_calls=[ToolCall("get_shipment_status", {"shipment_id": "KZ-4471"})]
            )
        return Response(text=f"Груз KZ-4471 сейчас: {tool_result}")
