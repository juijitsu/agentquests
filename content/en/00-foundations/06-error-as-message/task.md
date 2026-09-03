# Shift 6 · Loredo instead of Laredo

There is a typo in the request: the customer wrote "Loredo". No such crossing
exists — there is a Laredo. The dispatcher told the customer so and stopped
there.

```
python engine/check.py content/en/00-foundations/06-error-as-message/starter/novice/agent.py
```

Look at the first check line: the agent tried **one** value. It did not crash, it
did not loop, it answered politely — and it gave up where one step would have
fixed it.

The error text it received contains the list of valid crossings. The model never
saw it.

**Make the tool's error reach the model.**

## Done when

- the agent tried at least two values;
- the answer mentions the queue at the crossing;
- it stays within 3 iterations.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | the exception is caught but goes to the wrong place — the line is marked `TODO` |
| `starter/advanced/` | the exception is not caught at all |
| `starter/pro/` | the contract and the condition |

## If you get stuck

Look at which role a successful tool result enters the history under. From the
model's point of view, how is an unsuccessful one different?
