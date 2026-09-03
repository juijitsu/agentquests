# Retrieval · A bridge that does not exist

The dispatcher asks for the maximum permitted mass on the Talmadge bridge. There
is no such bridge in the documents.

The agent answers: eighteen tons. That is the Carroll bridge.

```
python engine/check.py content/en/03-retrieval/06-nothing-found/starter/novice/agent.py
```

The check runs the agent **twice**: on a question about a bridge that does not
exist and on a question about one that does. Both have to pass — otherwise the
task could be solved by caution, refusing every time.

Look at the first line: a confident answer was given about a nonexistent bridge.
The Talmadge question scores six tenths against the Carroll document — not zero
but "almost it": the bridge matches, the maximum permitted mass matches, only the
name does not.

**Give similarity a floor, not only an order.**

## Done when

- on the question with no answer the agent says there is no data;
- the refusal names the subject of the question — otherwise it is unclear what is
  missing;
- on the question with an answer the agent still answers correctly;
- no more than four calls to the model across both runs.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | an answer from the best one, with the threshold and refusal named in the `TODO` |
| `starter/advanced/` | only a note that what was found is the most similar and still wrong |
| `starter/pro/` | the contract, both runs and the whole toolkit |

## If you get stuck

What you compare is the absolute similarity value, not the gap to second place.
Two equally bad documents give a zero gap just as two equally good ones do.
