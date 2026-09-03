"""Fourth shift of the track. The rate is there; which one is today's is not."""

import sqlite3

LANG = "en"
TITLE = "Context track · Level 04 · Freshness"
BRIEF = """Rates are appended as history, old rows never go anywhere.
The query returns January's price, and the customer is quoted it as today's."""

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
        return ("There must be exactly one query. sqlite will not run several\n"
                "        statements separated by ';' at once — build a single select.")
    if isinstance(exc, sqlite3.OperationalError):
        return f"SQLite could not run the query: {exc}"
    return None


def verify(result):
    rows, queries = result
    # Counted from the rows that actually came back: a dict keyed by lane would
    # collapse duplicates and hide the very stale rates we are looking for.
    pairs = sorted((row[0], row[1]) for row in rows if len(row) >= 2)
    stale = sorted({price for _, price in pairs if price in STALE})
    return [
        (len(rows) == len(CURRENT), f"rows returned: {len(rows)} (lanes: {len(CURRENT)})"),
        (not stale, f"stale rates in the answer: {stale or 'none'}"),
        (pairs == sorted(CURRENT.items()), f"rates in the answer: {pairs}"),
        (queries == 1, f"queries executed: {queries} (one required)"),
    ]
