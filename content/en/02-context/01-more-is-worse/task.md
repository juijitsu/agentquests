# Papers · The bridge nobody noticed

A twenty-four-ton load runs from Laredo to Newark. There are three limited
bridges on the route, and the tightest holds eighteen tons.

The agent sends the model the whole haul folder — twenty-two papers — and gets
back an answer that the route is clear.

```
python engine/check.py content/en/02-context/01-more-is-worse/starter/novice/agent.py
```

Look at the first check line: the paper that mattered **never reached the
model**. It was sent — and it did not arrive, because it ended up in the middle
of a long list, and the middle is not read.

**Send what bears on the question, not everything you have on the haul.**

## Done when

- the paper with the 18-ton limit reached the model;
- the agent answers that the load will not pass;
- no more than six blocks were sent;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | the spot to fix marked `TODO`, with the calls spelled out |
| `starter/advanced/` | only a note that the limit is in the folder |
| `starter/pro/` | the contract and the window reading rule |

## If you get stuck

The `about` tool takes a topic, not the whole question. What the topic is here is
known to `model.topic`.
