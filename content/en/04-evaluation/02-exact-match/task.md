# Evaluation · Roll back an improvement

The new version answers all six cases correctly. The old one was wrong on one.

The evaluator shows: old five of six, new three of six. It got worse, roll the
fix back.

```
python engine/check.py content/en/04-evaluation/02-exact-match/starter/novice/agent.py
```

Look at the first check line: zero semantic checks. The answers were compared
character by character, and three correct answers were declared errors:

```
expected: 2.90    got: two dollars ninety cents
expected: 18:00   got: six in the evening
expected: 24 t    got: twenty-four tons
```

**Check the answer, not how it is written.**

## Done when

- every answer of both versions was checked by meaning;
- the verdict is that it got better;
- the new version's score is named: 6 of 6;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | character comparison, with the call you need named in the `TODO` |
| `starter/advanced/` | only a note that the run was done by the book |
| `starter/pro/` | the contract and the nature of the mismatch |

## If you get stuck

String normalization will not help here. "Two dollars ninety cents" and "2.90"
share not one character — this is not the same text spelled differently but
different texts about one fact.
