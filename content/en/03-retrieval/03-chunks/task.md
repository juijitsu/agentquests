# Retrieval · Thirty tons of the wrong bridge

The dispatcher asks for the maximum permitted mass on the Carroll bridge. The
right answer is twenty-four tons.

The agent answers: thirty. That is the Greenville bridge.

```
python engine/check.py content/en/03-retrieval/03-chunks/starter/novice/agent.py
```

Look at the first check line: not one chunk was rebuilt. The Carroll bridge is
named in one chunk, its limit is in the neighbour, and neither passes the fitness
check. The only thing lying whole in the index is somebody else's bridge, and the
agent honestly answers from it.

**Rebuild a chunk into something self-contained before judging it.**

## Done when

- chunks were rebuilt with their neighbours;
- the answer is about Carroll, not Greenville;
- 24 t is named;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | the previous level's technique, with the tool named in the `TODO` |
| `starter/advanced/` | only a note that nothing passes the fitness check |
| `starter/pro/` | the contract and how the index is built |

## If you get stuck

Look at what exactly goes into `model.answers`. If it is a chunk, you are judging
a chunk. What you need to judge is a fact.
