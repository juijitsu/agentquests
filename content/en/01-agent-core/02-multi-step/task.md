# Shift 2 · We reached Dallas

Dispatch hands out the route one stop at a time: you can only learn what comes
after Dallas by getting to Dallas. The freight has to reach Newark.

The agent gets to Dallas and answers: "Reached Dallas".

```
python engine/check.py content/en/01-agent-core/02-multi-step/starter/novice/agent.py
```

Look at the first check line — how many stops were covered. The agent did not
crash and was not wrong: it honestly took a step and honestly reported it. It is
just that a step is not the whole task.

**Make the loop continue all the way to Newark.**

## Done when

- all three hops were covered;
- the answer contains Newark;
- it stays within 10 iterations.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | the whole loop, the exit point marked `TODO` |
| `starter/advanced/` | a loop with no goal check |
| `starter/pro/` | the contract and the condition |

## If you get stuck

The model does not remember where you are: it sees only the history. If you keep
the loop going, tell it which city you reached.
