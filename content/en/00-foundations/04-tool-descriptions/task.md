# Shift 4 · An answer to a different question

The customer asked how long the wait is at the Laredo crossing. The dispatcher
sent them a freight invoice.

```
python engine/check.py content/en/00-foundations/04-tool-descriptions/starter/novice/agent.py
```

The first check line shows which tool was called. The loop logic is fine — you
fixed it on the earlier levels. What is broken is a description.

**Rewrite the description so the agent picks the right tool.**

You do not need to touch the code at all. The whole fix is in the text.

## Done when

- `check_border_status` was called, and only it;
- the answer mentions the queue at the crossing;
- it stays within 3 iterations.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | one description is ruined, the other intact — something to compare against |
| `starter/advanced/` | both descriptions empty, write them from scratch |
| `starter/pro/` | the tool list is empty, declare both yourself |

## If you get stuck

Read the neighbouring tool's description and find a word from the customer's
question inside it. Now it is clear why that one got picked.
