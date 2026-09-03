# Retrieval · Somebody else's cargo weight

The dispatcher asks for the weight on waybill 4471. The right answer is
twenty-four tons, sheet glass.

The agent answers: nineteen. That is waybill 4478, pipe.

```
python engine/check.py content/en/03-retrieval/07-hybrid/starter/novice/agent.py
```

Look at the second check line: the wrong document was chosen. Semantic search
worked flawlessly — it found a waybill with a cargo weight. A waybill. With a
weight. Just not the right one, because to meaning 4471 and 4478 are
indistinguishable.

Bringing keyword search back will not help either: the email says "waybill 4471"
as bare words and matches the question twice, while the waybill itself writes the
number with a colon after it and matches once.

**Narrow by an exact match on the number, choose by meaning.**

## Done when

- both signals are used — exact and semantic;
- waybill 4471 was chosen, not the email and not the neighbouring waybill;
- the answer names 24 t;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | selection by meaning, with both calls named in the `TODO` |
| `starter/advanced/` | only a note that meaning worked correctly |
| `starter/pro/` | the contract and why neither method alone will do |

## If you get stuck

The exact search looks for the identifier, not the whole question. Over the whole
question it will bring back the email and the payment note again.
