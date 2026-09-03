# Evaluation · Five of eight, four of them familiar

The agent ran the set: five of eight. Sixty-three percent.

Four of those eight cases sit word for word in the agent's prompt as examples. On
those it does not answer, it recalls, and all four are naturally correct.

```
python engine/check.py content/en/04-evaluation/05-leak/starter/novice/agent.py
```

Look at the first check line: not one case was checked for a leak.

The honest score is over the four that are not in the prompt: **one of four**.
Twenty-five percent instead of sixty-three. That is not measurement error, that
is the difference between "works" and "does not work".

**Compute the score over the unseen cases separately.**

## Done when

- all eight cases were checked for a leak;
- the honest score over the unseen cases is named: one of four;
- the overall score is named too — the gap between them is useful;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | a score over the whole set, with the tool you need named in the `TODO` |
| `starter/advanced/` | only a note that everything earlier was done correctly |
| `starter/pro/` | the contract and the nature of the leak |

## If you get stuck

Every case has to be checked, not the suspicious ones: the suspicious ones will
turn out to be the wrong ones.
