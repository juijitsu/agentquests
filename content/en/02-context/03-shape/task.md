# Papers · The heaviest is the wrong one

Five loads, each with a weight and a departure day. The question is simple: which
is the heaviest of the ones leaving today.

The right answer is TX-337, twenty-seven tons. The agent answers: thirty-one
tons. That is TX-204, and it leaves tomorrow.

```
python engine/check.py content/en/02-context/03-shape/starter/novice/agent.ts
```

The command is the same as for the Python levels — the runner sorts it out
itself. Nothing needs installing: Node strips the types.

Look at the first check line: the data shape is running text. All five loads were
passed, nothing was lost. It is just that in a paragraph the weight is tied to the
day only by word order, and you cannot filter on that.

**Pass records instead of a paragraph.**

## Done when

- the data went out as records, not as text;
- every record carries all three fields;
- the answer names TX-337;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | the spot to fix marked `TODO`, the call spelled out |
| `starter/advanced/` | only a note that nothing was lost |
| `starter/pro/` | the contract and what running text gives you |

## If you get stuck

The difference between `join` and `map` here is not stylistic. The first glues
records into one string, the second leaves them as records.
