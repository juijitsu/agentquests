# Theory · Shape is part of the data

The first level of the track taught you not to dump what is extra, the second not
to lose the source. Here nothing is lost and nothing is extra: all five loads were
passed, and each one carries both its weight and its departure day.

The answer is still about the wrong loads.

## What is wrong with running text

The question demands two actions at once: **filter** by day and **compare** by
weight. Both rest on the weight and the day belonging to the same load.

In a paragraph that belonging is expressed only by word order:

```
Load TX-118 weighs 24 t and leaves today. Load TX-204 weighs 31 t and leaves tomorrow.
```

Pulling the numbers out is easy; tying the twenty-four specifically to "today" is
already work that the text does not support but merely permits. One line break,
one inserted note or a different word order is enough for the link to drift.

What happens in practice: the filter condition is **quietly lost**. The model
answers about the heaviest load overall — thirty-one tons — because that is the
only thing computable from bare numbers with no fields.

## The same information, a different shape

```json
{ "id": "TX-118", "tons": 24, "day": "today" }
```

Not one new fact. But now the belonging is expressed by **structure** rather than
adjacency: the weight sits in the `tons` field of the TX-118 record and cannot
refer to anything else.

> **Structure is not decoration. It is a statement about what belongs to what.**

## Why this is cheaper than it looks

The temptation is to describe the data in words — the model understands language,
after all. It does. But every correspondence you leave to the text it re-derives
on every request, and it derives it probabilistically.

Parsing text into records once costs ten lines of code. Leaving it as text costs
one mistake in every answer, and that mistake is invisible: it looks like a
confident answer with a number in it.

## Why this level is in TypeScript

Because the task is about the shape of data, not about an agent loop. Records,
fields and types are what TypeScript exists for; here a `Load` with three fields
states the data contract right in the code. That is how the course goes on:
**the language is picked for the task**, not the other way round.

Nothing needs installing: Node strips the types itself, there is no build.
