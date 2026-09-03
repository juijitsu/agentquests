# Shift 4 · The bridge everyone forgot

A 25-ton load. On the second hop it turns out the bridge takes only 20.

The agent honestly writes that down in the notepad — and at the end answers that
the route is clear.

```
python engine/check.py content/en/01-agent-core/04-scratchpad/starter/novice/agent.py
```

Look at the second check line: the notepad entry is there. The information was
gathered. It simply never reached the model — the notepad does not make it into
the window.

**Deliver the notepad into the window.**

## Done when

- all seven hops were covered;
- the notepad holds one entry;
- the agent answers that the route does not work;
- it stays within 12 iterations.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | a window with terms and tail, the spot to fix marked `TODO` |
| `starter/advanced/` | the same, with no word on where to fix it |
| `starter/pro/` | the contract and the condition |

## If you get stuck

The window has eight slots and there are three claimants now. Work out how many
are left for the tail once the terms and the notepad have taken theirs.
