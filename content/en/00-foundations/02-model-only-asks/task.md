# Shift 2 · Sent, but never arrived

The customer has been calling for two days. Every time, the dispatcher answers
that the notification was sent. The send journal is empty.

Run it and look at the two check lines:

```
python engine/check.py content/en/00-foundations/02-model-only-asks/starter/novice/agent.py
```

The agent reported success — a tick. Notifications actually sent: zero — a cross.
Exactly the situation the customer is calling about.

**Fix it so the notification is really sent.**

## Done when

- the agent reports the send;
- the journal holds exactly one notification;
- it stays within 3 iterations.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | the whole loop, with two checks in the wrong order |
| `starter/advanced/` | the exit branch is written, parsing `tool_calls` is yours |
| `starter/pro/` | the contract and the condition |

## If you get stuck

Look at what the model returns on the first iteration. The answer holds both text
and a request. Which of the two does your loop notice first?
