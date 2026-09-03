# Finale · Friday, delivery day

The developer quit. The agent ships to the customer on Friday. Not all five
requests pass, and nobody knows why.

```
python engine/check.py content/en/00-foundations/08-read-someone-elses-agent/starter/novice/agent.py
```

The check will show the score and the first failing requests.

**Find and remove every defect so that all five requests pass.**

There are three. You have already seen each one separately on the earlier levels.

## Done when

- all five requests pass.

## Choose a difficulty

Everyone gets the same file on this level — the task is diagnostic, there is
nothing to write from scratch. What shrinks is the hints:

| Folder | What you are told |
|---|---|
| `starter/novice/` | three places marked with comments |
| `starter/advanced/` | there are three defects, no word on where |
| `starter/pro/` | nothing beyond the fact that not everything passes |

## If you get stuck

Run it and see how many requests failed. If almost all of them did, look for a
shared place every request goes through.
