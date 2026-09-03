# Retrieval · A policy instead of a price

The dispatcher asks: what does a mile cost on Laredo — Newark.

The agent finds a document about that very rate and that very lane and answers:
"base plus surcharges, revised quarterly".

```
python engine/check.py content/en/03-retrieval/02-similar-not-useful/starter/novice/agent.py
```

Look at the first check line: nothing was checked for fitness. The search worked
correctly — the policy it found really is about the rate on this lane. It simply
holds no number, and similarity does not know that.

**Select the fit ones, and take the most similar only among them.**

## Done when

- the candidates were checked for fitness;
- the price line was chosen, not the policy;
- the answer names the rate 2.90;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | selection by similarity, with the call you need named in the `TODO` |
| `starter/advanced/` | only a note that the search worked correctly |
| `starter/pro/` | the contract and both quantities |

## If you get stuck

The order of the steps decides. Take the most similar first and check it for
fitness afterwards, and you are left with nothing — it will not pass the check.
