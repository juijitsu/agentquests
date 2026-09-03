# Evaluation · Five of six on a lucky run

The agent ran the set once: five of six.

A second run of the same set by the same system gives three of six.

```
python engine/check.py content/en/04-evaluation/06-one-run/starter/novice/agent.py
```

Look at the first check line: runs per case — one.

Two cases out of six answer every other time. On run zero both came out lucky,
and the agent declared the system working. On run three both came out unlucky.

**Run every case several times and split into three states:** holds every time,
never works, does not hold.

## Done when

- every case was run all five times;
- the unstable cases are named by name;
- the report says three stably correct out of six;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | one run, with the three-way split described in the `TODO` |
| `starter/advanced/` | only a note that everything earlier was done correctly |
| `starter/pro/` | the contract and the nature of non-determinism |

## If you get stuck

The order of the checks decides: `all` is stricter than `any`, so it comes first.
Start with `any` and you will file the always-correct cases as unstable too.
