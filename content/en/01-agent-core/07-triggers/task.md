# Shift 7 · The inbox that fills itself

Three events wake the dispatcher: a delay, a breakdown near Memphis, an ice storm
on I-80. It handles all three and closes the shift.

By that moment two more are sitting in the inbox.

```
python engine/check.py content/en/01-agent-core/07-triggers/starter/novice/agent.py
```

Look at the second check line — what was left in the inbox. Moving the load off
the stalled tractor and routing around the ice: both tasks were spawned by the
handling itself, and both appeared after the agent had already made its to-do
list.

**Make the agent drain the queue instead of walking a snapshot of it.**

## Done when

- all five events were handled, spawned ones included;
- the inbox is empty;
- the queue was polled at least as often as events were handled;
- the agent reported five events;
- it stays within 8 iterations.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | a loop over a snapshot, the spot to fix marked `TODO` |
| `starter/advanced/` | the same loop and one leading question |
| `starter/pro/` | the contract, the tool list and the limiter |

## If you get stuck

Count how many times your code asks `pending`. If it is once, you are reading a
photograph of the queue taken before the first action.
