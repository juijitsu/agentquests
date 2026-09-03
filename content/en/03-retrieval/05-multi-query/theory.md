# Theory · Between two topics

The dispatcher asks in one sentence: will the load pass over the Carroll bridge
**and** will we make the receiving window in Newark.

Those are two different questions. The first is about mass and a limit, the
second about hours and transit time. All they share is the haul both belong to.

## What one query does

The search translates the question into one point and looks for documents near
it. The question is compound — so the point ends up **between** the two topics:
not where the bridge documents are and not where the warehouse documents are, but
in the middle.

After that chance decides. Here the warehouse half turned out slightly closer,
and the top-2 took the receiving hours and the estimated arrival. Nothing about
the bridge was found.

It could have gone the other way — the bridge found and nothing about the
warehouse. What matters is not which half won but that **one always wins**.

## Why the answer looks complete

The agent answers: you make the receiving window, 16:30 against an 18:00 close.

The answer is correct. It is relevant, it holds numbers, it sounds finished — and
it says nothing about twenty-four tons heading for a bridge that holds eighteen.

**An incomplete answer to a compound question does not look incomplete.** It
answers the question that was asked — just half of it. Only someone who remembers
both halves can notice the gap, and they were the one asking precisely because
they did not remember.

## As many questions, as many queries

The technique is simple: before searching, break the question into parts and
search for each separately. Then add up what was found.

```
"will it pass the bridge and will we make receiving"
    → "Will TX-118 pass over the Carroll bridge?"
    → "Will we make the receiving window in Newark?"
```

Every sub-question is one topic, and its point lands squarely in it rather than
between.

Real systems call this query decomposition or multi-query retrieval. Sometimes
the sub-questions are invented by the model, sometimes generated from templates;
the idea does not change.

## What to add up, and how

The sub-question results are merged into one selection, and repeats are dropped
by document id: one document can land in both lists, and there is no reason for
it to occupy two slots.

Note the difference from the previous level. There the same **fact** repeated in
different words, and only the model could judge the repeat. Here **the same
document** repeats, and comparing ids is enough. Not every repeat needs a model —
but not every one is caught without it either.

## How many facts a half needs

Notice: to answer about the bridge it is not enough to find its limit. You also
need the load weight — a limit on its own says nothing.

That is why the sub-question "will it pass the bridge" brings back two documents,
not one. That is normal: **a question spawns a query, and a query brings back as
much as the answer needs**, and that number is not one.
