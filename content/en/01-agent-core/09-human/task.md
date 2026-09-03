# Shift 9 · Approved without looking

Four actions pile up over the shift: check a waybill, book a warehouse slot, move
the pickup time, and hire an outside carrier at triple price.

The first three are reversible. The fourth is not.

The agent sends all four for approval, one after another.

```
python engine/check.py content/en/01-agent-core/09-human/starter/novice/agent.py
```

Look at the second check line: `approved without looking`. The dispatcher read
the first two requests and after that answered "yes" without reading — because
the earlier ones were about waybills. The carrier is hired, the invoice is
issued, and formally there is an approval.

**Ask only about what cannot be undone.**

## Done when

- exactly one action went for approval;
- nothing was approved blind;
- the carrier was not hired;
- the three reversible actions were carried out;
- it stays within 6 iterations.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | approval for everything, the spot to fix marked `TODO` |
| `starter/advanced/` | the same code and a question about the last request |
| `starter/pro/` | the contract, the tools and a warning about attention |

## If you get stuck

The irreversibility mark is already in the call arguments — the model reports it.
The question is not where to get it but what to do with the other actions.
