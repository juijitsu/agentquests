# Retrieval · Half an answer

The dispatcher asks: will TX-118 pass over the Carroll bridge and will we make
the receiving window in Newark.

The agent answers: you make the receiving window, 16:30 against an 18:00 close.

That is true. And it is half.

```
python engine/check.py content/en/03-retrieval/05-multi-query/starter/novice/agent.py
```

Look at the first check line: there was one query. The question holds two, and
the search point landed between the topics — closer to the warehouse half. The
top-2 took both receiving papers, and nothing was found about the bridge.

And twenty-four tons are heading for a bridge with an eighteen-ton limit.

**Split the question and search for every part.**

## Done when

- at least two queries went to the search;
- the selection holds all four facts: limit, weight, receiving hours, arrival;
- the answer says the bridge will not take it;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | one query, with `split` and the merge rule named in the `TODO` |
| `starter/advanced/` | only a note that both documents found are about one half |
| `starter/pro/` | the contract and the nature of a compound question |

## If you get stuck

To answer about the bridge it is not enough to find its limit — you also need the
load weight. One sub-question legitimately brings back two documents.
