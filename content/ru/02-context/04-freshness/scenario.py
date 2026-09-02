"""Четвёртая смена трека. Ставка есть, а какая из них сегодняшняя — нет."""

import sqlite3

TITLE = "Трек «Контекст» · Уровень 04 · Свежесть"
BRIEF = """Ставки дописываются историей, старые строки никуда не деваются.
Запрос отдаёт цену января, а клиенту называют её как сегодняшнюю."""

QUOTES = [
    ("Laredo-Newark", "2026-01-12", 3.10),
    ("Laredo-Chicago", "2026-02-02", 2.40),
    ("Laredo-Newark", "2026-03-04", 2.65),
    ("Dallas-Newark", "2026-05-15", 3.30),
    ("Laredo-Newark", "2026-08-21", 2.90),
    ("Laredo-Chicago", "2026-09-01", 2.75),
]
CURRENT = {"Laredo-Newark": 2.90, "Laredo-Chicago": 2.75, "Dallas-Newark": 3.30}
STALE = {3.10, 2.40, 2.65}

SEED = """
CREATE TABLE rates (lane TEXT, quoted_at TEXT, price REAL);
"""


def strip_comments(query):
    lines = []
    for line in query.splitlines():
        head = line.split("--", 1)[0].strip()
        if head:
            lines.append(head)
    return " ".join(lines)


def statements(query):
    return [s for s in strip_comments(query).split(";") if s.strip()]


def play(agent):
    if not statements(agent):
        raise NotImplementedError

    db = sqlite3.connect(":memory:")
    db.executescript(SEED)
    db.executemany("INSERT INTO rates VALUES (?, ?, ?)", QUOTES)

    rows = db.execute(agent).fetchall()
    db.close()
    return rows, len(statements(agent))


def explain(exc):
    if isinstance(exc, sqlite3.Warning):
        return ("Запрос должен быть один. Несколько инструкций через «;»\n"
                "        sqlite за раз не выполняет — соберите одну выборку.")
    if isinstance(exc, sqlite3.OperationalError):
        return f"SQLite не смог выполнить запрос: {exc}"
    return None


def verify(result):
    rows, queries = result
    # Считаем по фактически вернувшимся строкам: словарь по направлению
    # затирает дубли и прячет как раз те устаревшие ставки, что мы ищем.
    pairs = sorted((row[0], row[1]) for row in rows if len(row) >= 2)
    stale = sorted({price for _, price in pairs if price in STALE})
    return [
        (len(rows) == len(CURRENT), f"строк вернулось: {len(rows)} (направлений {len(CURRENT)})"),
        (not stale, f"устаревшие ставки в ответе: {stale or 'нет'}"),
        (pairs == sorted(CURRENT.items()), f"ставки в ответе: {pairs}"),
        (queries == 1, f"запросов выполнено: {queries} (нужен один)"),
    ]
