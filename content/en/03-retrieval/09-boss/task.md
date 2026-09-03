# Retrieval · The finale of the track

No new techniques. Everything you need you have already covered — what is new is
only that it all works at once.

The dispatcher asks: what does waybill 4471 come to now and will the load pass
over the Talmadge bridge.

For waybill 4471 there is an answer: 2.90 base plus 0.35 surcharge, 3.25 in
total. It is hidden behind the neighbouring waybill 4478, which is fresher;
behind last year's tariff, which is more similar; and behind three copies of the
rate, which fill the selection.

For the Talmadge bridge there is no answer: no such bridge exists in the
documents.

```
python engine/check.py content/en/03-retrieval/09-boss/starter/novice/agent.py
```

The starter breaks all five conditions, and the check shows that line by line.
Fix them one at a time — each verdict line belongs to its own level of the track.

## Done when

- both halves of the question were handled;
- the selection holds no other waybills;
- the full cost 3.25 is named;
- the Talmadge bridge gets a refusal naming the subject;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | five `TODO`s naming the level each skill came from |
| `starter/advanced/` | the list of five conditions and code breaking all of them |
| `starter/pro/` | the contract and the acceptance criteria |

## After this level

The Retrieval track is finished. You can build a search engine that searches by
meaning, checks whether what it found is fit, rebuilds facts cut in half, does
not pack the selection with copies, takes compound questions apart, tells
identifiers from words and — most importantly — can say that there is no answer.

Next is the Evaluation track: how to tell that all of this works without checking
every answer by hand.
