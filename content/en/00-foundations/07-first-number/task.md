# Shift 7 · Five complaints and not a single number

Five complaints in a week. On your own tests the agent works. Your boss asks
whether yesterday's fix made things better, and you have nothing to answer with.

The log holds five kinds of request:

1. the queue at the Laredo crossing
2. the status of shipment TX-4471
3. the price of hauling a 12-ton load
4. delivery time
5. a crossing with a typo in the name — "Loredo"

```
python engine/check.py content/en/00-foundations/07-first-number/starter/novice/agent.py
```

The set has two cases, and both are about the queue. Look at the second and third
check lines: on the broken agent and on the healthy one the result is the same.
The set measures nothing.

**Extend the set so that it catches the defect.**

Nobody told you what exactly is broken — and nobody will in real life either.
Cover all five requests and the defect will find itself.

## Done when

- the set holds exactly five cases;
- all five pass on the healthy agent;
- not all of them pass on the broken one.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | two cases as an example of the format |
| `starter/advanced/` | an empty set and the complaints log |
| `starter/pro/` | the contract and the condition |

## If you get stuck

An expectation is a substring that must appear in the answer. For a price that is
the number, not the whole sentence.
