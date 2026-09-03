# Shift 5 · El Paso is not answering

The El Paso crossing has not returned data for three days. The dispatcher asks
about it again and again, hits the ceiling and dies with `RecursionError`.

```
python engine/check.py content/en/00-foundations/05-three-ways-to-break/starter/novice/agent.py
```

The limiter worked correctly — stopping the loop is exactly what it was for.
What is bad is **how** it did it: a stack trace went out the door.

**Make the agent return a message a human can understand.**

## Done when

- the agent reached the tenth iteration and raised no exception;
- the message names how many steps were spent;
- the message names the tool everything got stuck on.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | the whole loop, with the last line marked `TODO` |
| `starter/advanced/` | a loop with no exhaustion handling — spot it and write it |
| `starter/pro/` | the contract and the condition |

## If you get stuck

The name of the last tool is known inside the loop, but after the loop it is
gone. So it has to be saved somewhere along the way.
