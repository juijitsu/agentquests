# Retrieval · The wrong limit

The dispatcher asks: what is the weight limit on the Carroll bridge.

There are four documents in the corpus, and the one you need is among them:
"Carroll bridge: maximum permitted mass 18 t". The agent answers about the speed
limit on I-55.

```
python engine/check.py content/en/03-retrieval/01-words-vs-meaning/starter/novice/agent.py
```

Look at the first check line: the search went by words. The question says
"weight", the document you need says "mass" — no words in common. Meanwhile the
word "limit" sits on the speed sign, and keyword search honestly put it first.

**Search by meaning, not by matching words.**

## Done when

- the search went by meaning, not by words;
- the answer names 18 t;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | keyword search, with the calls you need named in the `TODO` |
| `starter/advanced/` | only a note that the document you need is in the corpus |
| `starter/pro/` | the contract and the whole available toolkit |

## If you get stuck

`similarity` takes two texts, not documents. A document is a dict; what you
compare is `doc["text"]`.
