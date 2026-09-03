# Theory · About the very thing, and with no answer

On the previous level the search was wrong: the question was about mass, it
returned speed. We fixed that by moving from words to meaning.

Here meaning works flawlessly. The document found is **genuinely about that very
rate and that very lane**, written in the same words, and confidently first by
similarity.

And the answer is not in it.

## A policy resembles a price list more than a price list does

The question: what does a mile cost on Laredo — Newark.

The first document is a policy: "how a rate is formed: base plus surcharges,
revised quarterly". It contains "rate", "Laredo", "Newark" and "mile". The
overlap is nearly complete.

The second is a price line: "Laredo — Newark: 2.90 per mile". Fewer concepts,
therefore lower similarity.

The result is a paradox that is really a regularity: **documents about a subject
almost always resemble the question more than documents with the answer.**
Policies, manuals and method descriptions are written in the same words as the
question, and they are wordy besides. An answer is usually short and does not
scatter the question's words around.

## Similarity measures the wrong thing

It is worth saying outright, because it is the main idea of the level.

**Similarity answers the question "is this about it".** It knows nothing about
whether the value being sought is inside. A rate policy is unquestionably about
rates; there is no number in it and none was intended.

The question "is the answer here" is **a different question**, and it is settled
by a different check.

## Find, then verify

Hence a technique that real systems call reranking or groundedness checking, and
which is really just a second step:

1. narrow the corpus to candidates with search;
2. ask of every candidate whether it answers the question;
3. among those that pass, take the most similar.

The order matters. Fitness filtering first, similarity second — otherwise you
again pick the most similar and only then discover it does not answer.

## Who decides whether a document is fit

The temptation is clear: the answer must contain a number, so let us look for
digits with a regular expression. For this corpus that would work.

And then the question will not be about price but about a deadline, a name, a yes
or no — and the regular expression has to be rewritten for every kind of
question. **You wrote not a search but a parser for one document.**

Fitness depends on the question, so the model judges it: `model.answers`. Your
job is not to forget to ask.
