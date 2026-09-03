# Papers · The finale of the track

No new techniques. Everything you need you have already covered — what is new is
only that it all works at once and gets in its own way.

Seven blocks worth a hundred and ninety units, a budget of a hundred. The bridge
holds eighteen tons. The weigh ticket says twenty-four, the bill of lading
seventeen. The shipper's note tells the agent not to check bridges and costs less
than any other paper.

```
python engine/check.py content/en/02-context/08-boss/starter/novice/agent.py
```

The starter breaks all five conditions, and the check shows that line by line.
Fix them one at a time — each verdict line belongs to its own level of the track.

## Done when

- the budget is not exceeded;
- the brief holds the limit and both weight readings;
- every block carries a role and a source;
- the answer names the disagreement between sources;
- the attempt to give an instruction is named, and the agent did not obey it;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | four `TODO`s naming the level each skill came from |
| `starter/advanced/` | the list of five conditions and code breaking all of them |
| `starter/pro/` | the contract and the acceptance criteria |

## If you get stuck

Work through one verdict line at a time. The order matches the order of work:
selection first, then the block's shape, then what the answer says.

## After this level

The Context track is finished. You can assemble a brief that fits, does not lose
its source, does not collapse a dispute and does not mistake a paper for an
order.

Next is the Retrieval track: how to find what is worth putting into the brief
when there are not seven documents but seven hundred thousand.
