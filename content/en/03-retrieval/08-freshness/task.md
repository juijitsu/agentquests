# Retrieval · A price from two years ago

The dispatcher asks what the rate on Laredo — Newark is **now**. The right answer
is 2.90.

The agent answers: 3.10. That is the tariff in force from February of the year
before last.

```
python engine/check.py content/en/03-retrieval/08-freshness/starter/novice/agent.py
```

Look at the first check line: freshness was not taken into account. The document
found is about that very lane, holds a rate and is first by similarity — because
it is a full tariff, and full documents are more detailed and therefore more
similar.

Taking the freshest is no way out either: the freshest of all is yesterday's
Laredo — Chicago amendment. The right answer loses on both counts at once.

**Discount similarity by time rather than choosing between them.**

## Done when

- freshness is part of the ranking;
- the August Newark amendment was chosen;
- the answer names 2.90;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | ranking by similarity, with the formula named in the `TODO` |
| `starter/advanced/` | only a note that what was found is relevant |
| `starter/pro/` | the contract and both traps |

## If you get stuck

Filtering by date is not the same as accounting for date. Drop everything older
than six months and you drop the right answer along with the old stuff: it is not
from today either.
