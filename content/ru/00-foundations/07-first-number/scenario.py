"""Смена седьмая. Диспетчер иногда ошибается, и никто не знает, как часто."""

TITLE = "Уровень 07 · Первое число"
BRIEF = """Пять жалоб за неделю, а на ваших проверках всё работает.
Пока нет счёта, спорить о качестве бессмысленно."""

RESULT = {"n": 0}

QUEUES = {"Laredo": "очередь 40 машин", "El Paso": "очередь 12 машин"}
SHIPMENTS = {"TX-4471": "в пути, прибытие через 4 дня"}


def _common(question):
    """То, в чём оба агента одинаковы."""
    q = question.lower()
    for name, state in QUEUES.items():
        if name.lower() in q:
            return f"переход {name}: {state}"
    for code, state in SHIPMENTS.items():
        if code.lower() in q:
            return f"груз {code}: {state}"
    if "срок" in q or "когда" in q:
        return "срок доставки: 11 дней"
    if "loredo" in q:
        return "перехода 'Loredo' не существует. Доступны: Laredo, El Paso"
    return None


def _about_price(question):
    """Про деньги спрашивают по-разному — агент не должен быть хрупким к слову."""
    q = question.lower()
    return "стоимост" in q or "стоит" in q or "цена" in q


def healthy(question):
    """Исправный агент: стоимость считается по весу."""
    known = _common(question)
    if known:
        return known
    if _about_price(question):
        return "стоимость перевозки 12 тонн: 1080 долларов"
    return "не понял вопрос"


def broken(question):
    """Тот же агент с одним дефектом: вес груза при расчёте игнорируется."""
    known = _common(question)
    if known:
        return known
    if _about_price(question):
        return "стоимость перевозки: 500 долларов"
    return "не понял вопрос"


def score(cases, agent):
    return sum(1 for q, expected in cases if expected.lower() in agent(q).lower())


def play(agent):
    cases = list(getattr(agent, "CASES", []))
    RESULT["n"] = len(cases)
    return score(cases, broken), score(cases, healthy)


def verify(result):
    broken_score, healthy_score = result
    n = RESULT["n"]
    return [
        (n == 5, f"кейсов в наборе: {n} (нужно 5)"),
        (n and healthy_score == n,
         f"на исправном агенте: {healthy_score} из {n} — набор не должен ругаться на здоровое"),
        (n and broken_score < n,
         f"на сломанном агенте: {broken_score} из {n} — набор обязан поймать дефект"),
    ]
