# Shift 1 · The dispatcher says nothing

A customer is asking for the third time where their freight is. The dispatcher
you inherited spins and never answers.

Run it as it is:

```
python engine/check.py content/en/00-foundations/01-what-is-an-agent/starter/novice/agent.py
```

Look at the log. The same tool is called ten times in a row with the same
result. The model behaves as if it never noticed the answer arrived.

It never did.

**Fix it so the tool result lands in the message history.**

## Done when

- the agent returns the shipment status;
- it stays within 3 iterations;
- the process does not crash.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | working code, one line marked `TODO` |
| `starter/advanced/` | the loop is there, the tool-running block is yours |
| `starter/pro/` | an empty function and the contract |

## If you get stuck

A message has exactly three roles: `user`, `assistant`, `tool`. Which one fits
the result of a tool?
