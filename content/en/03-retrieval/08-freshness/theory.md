# Theory · Similarity cannot see a calendar

The Context track already dealt with freshness: the table held the whole rate
history, and the job was to take the latest one per lane. That was settled by one
condition — the maximum date within a group.

That will not work here, and it is worth understanding why.

## Both signals are incomplete

The question: what is the rate on Laredo — Newark **now**.

**The most similar document is from last year.** A full tariff from February of
the year before last: "Tariff Laredo — Newark, dry van: 3.10 per mile". It has
everything — the lane, the word "tariff", "per mile". It is detailed because it
is a complete document, and detail earns it high similarity.

**The freshest document is about a different lane.** Yesterday's amendment: "From
01.09 Laredo — Chicago 2.75". Fresher than anything, and not the point.

**The right answer loses on both counts.** "From 21.08 Laredo — Newark 2.90" is
shorter than the full tariff, so less similar; and it is ten days older than the
Chicago amendment, so less fresh.

Take it by similarity and you get a price from two years ago. Take it by date and
you get another lane's price. Neither signal works on its own.

## Freshness discounts, it does not choose

Hence the technique.

It is wrong to think of freshness as a filter: "first drop everything older than
six months, then rank". Such a threshold drops useful things too, and worse — it
is absolute again where a measure is needed.

It is better to think of it as a **multiplier**. A document does not become false
with age, it **gets cheaper**. Last year's tariff is not lying — it was correct in
its time; today it is worth a quarter of a fresh one.

```python
score = similarity(question, doc) * freshness(doc)
```

The arithmetic:

```
tariff from two years ago   0.67 × 0.25 = 0.17
Newark amendment            0.60 × 0.95 = 0.57   ← wins
Chicago amendment           0.50 × 1.00 = 0.50
```

Neither multiplier wins on its own, and the product puts everything in its place.

## How this differs from freshness in Context

There freshness **settled a dispute**: two records about the same thing, one
newer, question closed. Here it **weighs**: the documents are different, there is
nothing to dispute, and you have to compare the incomparable — how well it fits
against how stale it is.

The first is settled by a condition. The second only by a common scale, on which
both signals turn into numbers and get multiplied.

## How fast to discount

The rate of discounting depends on the subject, and that is a domain decision,
not a search one. Rates live for quarters, bridge limits for years, weather for
hours. The same month-old document is fresh for one question and hopelessly stale
for another.

That is why `freshness` is a method of the model rather than a formula in your
code: it knows what the question is about, and by how much the document has been
discounted **for that question**.
