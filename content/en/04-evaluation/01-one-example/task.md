# Evaluation · Mended one, broke two

The agent was fixed: the old version did not know about the fuel surcharge, the
new one does.

The evaluator agent checks that case and reports: it got better.

```
python engine/check.py content/en/04-evaluation/01-one-example/starter/novice/agent.py
```

Look at the first check line: one case out of six was run. The very one the fix
was made for — it was obliged to pass.

Nobody asked about the other five. And the new version quotes a rate from two
years ago and gets the waybill weight wrong.

**Run both versions over the whole set and compare the numbers.**

## Done when

- all six cases were run on each version;
- the verdict is that it got worse;
- the answer names the score: 5 of 6 against 4 of 6;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | a check of one case, with the run you need described in the `TODO` |
| `starter/advanced/` | only a note about what the fix was made for |
| `starter/pro/` | the contract and how the set is built |

## If you get stuck

Both versions have to go through **the same** set. Comparing the old one on some
cases with the new one on others gives a number that means nothing.
