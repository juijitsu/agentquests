# Theory · The same thing in different words

The Context track began with the `about` tool: you asked for a topic and got the
fitting papers. The tool worked, and we used it without asking how it was built.

This track is about how it is built. And it begins with the fact that the most
obvious way to search is systematically wrong.

## Matching words is not matching meaning

The question: what is the **weight limit** on the Carroll bridge.
The document you need: Carroll bridge, **maximum permitted mass** 18 t.

They share one word, "Carroll". Neither "limit" nor "weight" appears in the
document: it says "permitted" and "mass". People write about the same thing in
different words, and that is the norm, not sloppiness.

Meanwhile another document does contain the word "limit": the **speed limit on
I-55**. Keyword search honestly counts the matches and puts it first.

## Why this is worse than an empty result

An empty result is visible. The agent says "found nothing", the person rephrases,
everyone survives.

Here the result is not empty. The search confidently returns a document that
formally resembles the query, and the agent just as confidently answers from it.
**About highway speed — where the question was about mass on a bridge.**

The mistake looks like a mistake at no stage: the search found something, the
agent read it, the answer came out coherent.

## What "searching by meaning" means

Meaning is not magic but a translation of text into a shared space where
different words about the same thing end up close together.

On this level the space is made deliberately simple: every text has a set of
concepts.

```
"Carroll bridge: maximum permitted mass 18 t"  →  {bridge, mass, limit}
"speed limit on I-55"                           →  {road, speed, limit}
a question about the weight limit on a bridge   →  {bridge, mass, limit}
```

Different words, matching concepts. Closeness is the share of concepts in common:
the document you need has three out of three, the speed sign one out of five.

In real systems a vector of hundreds of numbers stands in place of the concept
set, and a cosine in place of the overlap share. **The idea is the same**: text is
translated into a representation where what matters is content, not spelling.

## When words are needed after all

Do not conclude that keyword search is useless. A bill of lading number TX-4471,
a tax ID, a part number, a filename — here you want an exact match and meaning
only gets in the way.

How to combine the two is a level of its own in this track. For now it is enough
to understand that searching by meaning is the default, and words are brought in
deliberately.
