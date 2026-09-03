# Papers · Somebody else's surcharge

Three carriers, three rate sheets. The customer asks whether Delta will take a
reefer and at what price.

The agent selects everything about reefers — three lines, exactly on point — and
answers: Delta hauls them, surcharge 0.60 per mile.

Zero sixty is Ridge's rate. Delta does not haul reefers at all.

```
python engine/check.py content/en/02-context/02-boundaries/starter/novice/agent.py
```

Look at the first check line: zero blocks out of three carry a source. The
selection worked correctly and, along the way, tore the lines out of the rate
sheets together with their headings.

**Give every line its source back.**

## Done when

- every block sent carries its source;
- the agent answers that Delta does not haul reefers;
- no more than four blocks — the previous level still stands;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | the spot to fix marked `TODO`, the signature format spelled out |
| `starter/advanced/` | only a note that the selection is right and the answer is not |
| `starter/pro/` | the contract and the attachment rule |

## If you get stuck

`source` expects the line exactly as `about` returned it. Sign after you have
asked, not before.
