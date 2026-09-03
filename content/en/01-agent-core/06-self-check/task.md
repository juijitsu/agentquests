# Shift 6 · A route that does not make it in time

The customer asks for delivery within forty-eight hours. The agent assembles a
route out of four hops and reports: "Route assembled. Total 61 h."

Sixty-one is not forty-eight.

```
python engine/check.py content/en/01-agent-core/06-self-check/starter/novice/agent.py
```

Look at the first check line: every hop is there, the data is right, there were
no errors. And the result is still no good — nobody compared it against the
terms.

**Add a review before the handover.**

The model does the comparing. If the customer's condition shows up in your code
as a number, you have written a validator for one requirement, and the customer
will have five.

## Done when

- all four hops were checked;
- the review ran exactly once;
- the answer says the route does not fit the deadline;
- it stays within 8 iterations.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | the review point marked `TODO`, with a hint about review |
| `starter/advanced/` | only a leading question |
| `starter/pro/` | the contract and a ban on comparing in code |

## If you get stuck

A review needs two items: what came out and what was asked for. The second one is
sitting in the `question` argument and never went anywhere.
