# Shift 3 · An invoice with no total

The customer sent a request: 12-ton load, route Mexico to the East Coast. The
dispatcher honestly checked all four legs and returned an answer:

> Route is open. Cannot price it: the load weight was not given.

The weight was given. It was in the very first message.

```
python engine/check.py content/en/00-foundations/03-no-memory/starter/novice/agent.py
```

Look at the second check line: iterations are fine, the agent did not spin and
did not crash. Exactly one thing is broken — it does not remember the start of
the conversation.

**Fix it so the load weight reaches the last model call.**

## Done when

- the answer contains the total;
- it stays within 6 iterations.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | a working loop with one line "optimised" |
| `starter/advanced/` | the loop is there, accumulating history is yours |
| `starter/pro/` | the contract and the condition |

## If you get stuck

Count how many messages go to the model on the fifth iteration, and compare that
with how many have piled up in the list.
