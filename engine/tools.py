"""Инструменты уровня. Данные выдуманные — это нормально и так и задумано."""

SHIPMENTS = {
    "KZ-4471": "в пути, переход Хоргос, прибытие через 4 дня",
    "KZ-5120": "на таможенном оформлении в Актау",
    "KZ-6033": "доставлен 12 марта",
}

TOOLS = [
    {
        "name": "get_shipment_status",
        "description": (
            "Возвращает текущий статус груза по его номеру. "
            "Использовать, когда спрашивают, где находится груз."
        ),
        "parameters": {"shipment_id": "string"},
    }
]


def run_tool(name: str, arguments: dict) -> str:
    if name == "get_shipment_status":
        return SHIPMENTS.get(arguments["shipment_id"], "груз не найден")
    return f"инструмента '{name}' не существует"
