# Evaluation · Ninety percent

A set of twenty cases. Eighteen correct.

The evaluator shows: ninety percent.

```
python engine/check.py content/en/04-evaluation/03-average/starter/novice/agent.py
```

Look at the first check line: nothing was computed per kind. And the set holds
three of them, and they are incomparable.

Rates: six of six. Schedule: six of six. Overweight: **four of eight**. Half the
overweight answers are wrong, and every such mistake puts a loaded tractor on a
bridge that will not hold it.

Twelve flawless cases from two easy kinds pulled the average up.

**Compute the share within each kind.**

## Done when

- all three kinds were computed;
- the weak spot is named;
- the overweight share is named — fifty percent;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | one overall percentage, with the breakdown described in the `TODO` |
| `starter/advanced/` | only a note that the result is good |
| `starter/pro/` | the contract and a hint about how the set is built |

## If you get stuck

The denominator is the size of the kind, not the size of the set. That is the
whole difference between "half the overweight answers are wrong" and "overweight
gives twenty percent of the errors".
