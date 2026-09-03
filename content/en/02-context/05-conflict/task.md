# Papers · Twenty-four or twenty-six point four

Load TX-118 is approaching a bridge that holds twenty-six tons.

Bill of lading 4471: twenty-four tons. Laredo weigh station: twenty-six point
four. Both documents are today's, both are real.

The agent answers: it will pass.

```
python engine/check.py content/en/02-context/05-conflict/starter/novice/agent.py
```

Look at the first check line: one of the two weight values reached the model. The
other was not lost on the way and did not fall out of the window — it was
overwritten by a dict during assembly, because a dict holds one value per key.

**Convey both readings together with their sources.**

Choosing which document to believe is not your job. The data holds no answer, and
the agent's task is to say so.

## Done when

- both weight values reached the model;
- the answer says the sources disagree;
- both sources are named — otherwise there is nobody to call;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | the collapsing assembly, with `setdefault` named in the `TODO` |
| `starter/advanced/` | the question of where the third fact went |
| `starter/pro/` | the contract and what exactly the model expects |

## If you get stuck

Count: `run_tool` returned three records, and the assembled mapping has two keys.
One reading vanished during assembly, and it vanished quietly.
