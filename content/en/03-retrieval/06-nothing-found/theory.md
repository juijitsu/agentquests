# Theory · The best of nothing

The dispatcher asks about the Talmadge bridge. There is no such bridge in the
documents — not a line, not a mention.

The agent answers: eighteen tons.

That is the Carroll bridge's limit. **A correct answer to a different question.**

## Similarity is relative

Here is the main idea of the level, and it is worth saying slowly.

Ranking sorts. It always produces a first — because in any non-empty list
somebody is first. The first of the fitting and the first of the unfitting look
exactly alike: it is just the top row.

**Order answers the question "who is best". It does not answer "is that one good
enough".** The second question was never asked, and the ranking holds no answer
to it.

## Why the score does not drop to zero

The Talmadge question scores six tenths against the Carroll document. Not zero,
not "way off" — respectable.

And that follows. The question really is about a bridge, really about a maximum
permitted mass; everything matches except one word, the name. And one word out of
four concepts does not swing it.

**A missing answer does not look like low similarity.** It looks like "almost
it". Which is precisely why it cannot be spotted by looking at order alone.

## A floor, not only an order

The cure is an absolute criterion: similarity needs a floor. Below it is not "the
worst of what was found" but "not found".

```python
if model.similarity(question, best["text"]) < THRESHOLD:
    return model.say_missing(question)
```

The threshold is tuned to the data and is no sacred number. What matters is
different: **it has to exist at all.** A system with no floor is physically
incapable of saying no — there is no place in its code for it.

## Caution is a failure too

There is a temptation to solve the task from the other side: answer less often,
refuse at the slightest doubt. Such an agent will never lie.

And it will be useless. A search that answers "not found" to everything is no
better than one that answers everything at random: in both cases the answers are
unrelated to the corpus.

That is why the check on this level runs the agent twice — on a question with no
answer and on a question with one. **The threshold has to separate**, not reject.

## A refusal should be useful

"Found nothing" is a bad refusal. It does not say what happened: is the data
missing, was the query poor, did the search break?

A useful refusal names the subject: "there is nothing about the Talmadge bridge
in the documents". Now you can see what is missing and what to do about it — add
a document about that bridge.

The difference is the same as between "error" and "file not found: /etc/hosts".
The first reports the fact of a failure, the second its cause.
