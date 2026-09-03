# Shift 5 · The road is closed

Freight goes from Laredo to Newark. On the second hop there is a closure until
the end of the week.

The agent drives around the closed stretch and reports: freight delivered.

```
python engine/check.py content/en/01-agent-core/05-replanning/starter/novice/agent.py
```

Look at the second check line — what the agent actually drove. There is a hole in
the route where the closed road was. The freight will not reach Newark that way,
but the agent does not know it: to its loop "no through road" is an ordinary
string.

**Make the agent notice the plan became impossible and ask for a new one.**

Where to detour is not your business. The model decides that. If the name of a
detour city shows up in your code, you have written a branch instead of
replanning.

## Done when

- two plans were built: the original and the detour;
- the whole detour route was actually driven;
- the freight was delivered to Newark;
- it stays within 12 iterations.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | the reaction point marked `TODO`, with a hint about make_plan |
| `starter/advanced/` | only a note that not every result is equal |
| `starter/pro/` | the contract and a ban on city names in your code |

## If you get stuck

Compare two strings: what the tool returned on the closed hop and what it returns
on an ordinary one. The difference between them is the mark you are looking for.
