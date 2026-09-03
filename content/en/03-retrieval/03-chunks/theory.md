# Theory · A fact cut in half

The previous level gave you a technique: find candidates, check each for
fitness, take the most similar of those that pass. The technique is right.

Here it passes **not a single** chunk.

## The fact sits on the boundary

The document about the Carroll bridge is split by sentence:

```
The Carroll bridge on I-55 was rebuilt in 2024.
The maximum permitted mass after that is 24 t.
```

The first chunk names the bridge and holds no number. The second holds the number
and does not name the bridge. On its own neither answers the question, and the
fitness check honestly rejects both.

Note the words **"after that"**. The second sentence leans on the first: the mass
is not abstract but the one after the rebuild of that very bridge. The split tore
that link, and it cannot be restored from one chunk — the reference lost what it
pointed at.

That is the most common casualty of chunking. Pronouns, "the above", "in this
case", the section heading that says what the whole thing is about — all of it
stays on the other side of the boundary.

## What comes out whole is somebody else's fact

Meanwhile the Greenville bridge fits into one sentence: "Greenville bridge:
maximum permitted mass 30 t". The chunk is self-contained, passes the check, and
beats both stumps on similarity.

And the agent answers: thirty tons.

**That is a real limit of a real bridge.** Not one invention, not one data error.
The bridge is simply the wrong one. A mistake of this kind is caught neither by
fact checking nor by comparison with the source — the source is correct, the
question was about something else.

## A chunk boundary is a decision

Hence the idea this level exists for.

Chunking looks like a technical detail: split the text, put it in an index, move
on. In reality **you are deciding what will be findable at all.** A fact cut by a
boundary stops existing for the search — not "hard to find" but non-existent,
because no single chunk holds it whole.

## Two ways to restore wholeness

**Split by units of meaning.** Not by sentences and not by character count but by
sections, paragraphs, records — and with overlap, so a fact on a boundary lands
in both neighbouring chunks. That is the right fix, and it is made when the index
is built.

**Rebuild at query time.** When the index is already built — and it usually
already is — a chunk is extended with its neighbours and judged as a whole. That
is what you will do here.

Both strategies are one idea in different places: **the unit of search and the
unit of meaning have to coincide.** If they did not coincide at chunking time,
make them coincide at query time.
