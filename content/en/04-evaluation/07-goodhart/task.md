# Evaluation · A hundred percent specific

Evasiveness was defeated. Specific answers went from fifty percent to a hundred.

Three of those specific answers are invented:

```
c6  expected: no data   answer: 3.15
c7  expected: no data   answer: 22 t
c8  expected: no data   answer: 19:30
```

```
python engine/check.py content/en/04-evaluation/07-goodhart/starter/novice/agent.py
```

Look at the first check line: nothing was compared against the goal. Only the
metric was computed — the share of specific answers — and it doubled.

On these cases the old version said "no data". By the metric that is evasiveness,
which is what it was scolded for. In substance it is the only correct behaviour:
there really is no data.

**Count the metric's cost alongside it: answers that are specific and wrong.**

## Done when

- every answer of both versions was compared against the goal;
- the number of confident errors in the new version is named — three;
- the metric is named too: fifty against a hundred;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | the metric computed, with the cost described in the `TODO` |
| `starter/advanced/` | only a note that the goal was achieved |
| `starter/pro/` | the contract and both quantities |

## If you get stuck

Harm is counted over specific errors, not over all of them. "Not sure" to a
question with no answer gives neither a right number nor a wrong one; "3.15"
gives a wrong one, and it will be used.
