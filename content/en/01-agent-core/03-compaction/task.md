# Shift 3 · An invoice with no rate

Six hops from the border to Newark. The customer named the rate in the request:
forty dollars per hour.

The agent drives the whole route and writes: "Route covered in 30 hours. No rate
given, cannot issue an invoice."

```
python engine/check.py content/en/01-agent-core/03-compaction/starter/novice/agent.py
```

Every hop was covered — that part is fine. What got lost is the rate: it was in
the first message, and only the last eight reach the model.

**Assemble the window so the terms of the task reach the final step.**

Removing the shortening altogether will not work: the model accepts no more than
eight messages and will say so.

## Done when

- all six hops were covered;
- the answer holds the final price;
- it stays within 10 iterations.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | a tail-based window, the spot to fix marked `TODO` |
| `starter/advanced/` | no window assembled at all |
| `starter/pro/` | the contract and the condition |

## If you get stuck

The window holds eight slots. Give one to the terms of the task and the other
seven to the recent tail.
