# Shift 1 · An answer about the first leg

The customer asks how long freight takes in total from the border to Newark. The
dispatcher checks the first leg and answers: six hours.

Six hours is Laredo alone. After that come Dallas, Chicago and Newark.

```
python engine/check.py content/en/01-agent-core/01-plan-first/starter/novice/agent.py
```

The first check line shows how many legs the agent looked at.

Notice: the agent did not crash and did not loop. It confidently answered with a
number — just not the one that was asked for. That kind of thing is found by
customers, not developers.

**Make the agent get a plan first, then walk it end to end.**

## Done when

- all four legs were checked;
- the answer holds the end-to-end time for the whole route;
- it stays within 6 iterations.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | the whole loop, the spot for the plan marked `TODO` |
| `starter/advanced/` | a loop with no planning, add it yourself |
| `starter/pro/` | the contract and the condition |

## If you get stuck

The model follows a plan only if it can see it in the history. Look at which role
the other messages go into the history under, and give the plan its own.
