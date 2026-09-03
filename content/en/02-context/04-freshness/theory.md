# Theory · Which one is today's

For three levels running we worked out what to put into the context and in what
form. Here the data is finally correct, signed and structured — and still wrong,
because it is **stale**.

## Data is appended, not overwritten

That is how almost everything that keeps a history works: rates, prices,
statuses, configs, exchange rates. A new rate does not overwrite the old one, it
lands beside it. The reasons are good — you need to know what price applied in
March, you need to be able to settle a dispute with a customer.

The consequence: **the table holds every answer to the same question at once.**
Three rows for Laredo — Newark: January's, March's, August's. Each was correct
once.

```sql
SELECT lane, price FROM rates;
```

This query does not lie. It honestly returns everything there is. It is just that
"everything there is" is not an answer to "what does it cost now".

## Whatever comes first is almost always the oldest

With no order specified, the database returns rows however it finds convenient,
and in practice that is usually insertion order. Which means the **earliest** row
arrives first.

Hence a particularly nasty form of the mistake: the agent quotes the customer
January's price as today's. A difference of forty cents a mile on a three
thousand mile run is twelve hundred dollars, and it comes to light when the
invoice is issued.

## The obvious fix is also wrong

The first thought is to take the freshest row.

```sql
SELECT lane, price FROM rates ORDER BY quoted_at DESC LIMIT 1;
```

The freshest row in the table is September's, and it belongs to Laredo — Chicago.
That is not what was asked about.

**Freshness is computed inside a group, not across the table.** Every lane has
its own history and its own last row. That is the key idea of the level, and SQL
expresses it directly: the subquery looks for the maximum `quoted_at` **for the
same `lane`**.

## Why this level is in SQL

Because "the latest row per key" is a storage problem, not an agent problem.
Dragging the whole history into the context so the model can pick the fresh one
itself means paying for six rows where three are needed, and hoping it does not
mix up the dates.

Filtering by time is done where the data lives. Nothing needs installing: the
sqlite engine already ships with the Python standard library.
