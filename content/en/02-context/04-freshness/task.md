# Papers · January's price as today's

Rates are appended to the table, not overwritten: every lane carries its whole
history. Laredo — Newark has three rows: 3.10 in January, 2.65 in March and 2.90
in August.

The agent quotes the customer 3.10.

```
python engine/check.py content/en/02-context/04-freshness/starter/novice/agent.sql
```

The command is the same as for the Python and TypeScript levels. Nothing needs
installing: the sqlite engine ships with the standard library.

Look at the second check line: the answer holds stale rates. The query did not
lie — it returned everything there is. It is just that "everything there is" does
not answer "what does it cost now".

**Return one current rate per lane.**

## Done when

- three rows came back — one per lane;
- not a single stale rate in the answer;
- every lane carries its current price;
- exactly one query.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | a select over the whole history, with grouping and maximum named in the `TODO` |
| `starter/advanced/` | only a note that rates are appended |
| `starter/pro/` | the table schema and a warning about the freshest row |

## If you get stuck

The latest row in the whole table is September's, and it is about Laredo —
Chicago. So the maximum has to be found within a lane, not across the table.
