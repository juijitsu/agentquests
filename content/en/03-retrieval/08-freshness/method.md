# Method · A product instead of a choice

**Step 1. Compute both signals for every document.** Throw nothing away in
advance: filtering by date drops the right answer along with the old stuff.

**Step 2. Multiply.**

```python
model.similarity(question, d["text"]) * model.freshness(d)
```

The product is usually taken rather than the sum, and the reason is zero: a
document that is irrelevant has to drop out no matter how fresh it is. A product
guarantees that; a sum does not.

In fairness: on this small corpus a sum gives the same answer, and you will pass
the check with it too. The difference shows up where there are thousands of
documents and fresh rubbish with near-zero similarity turns up.

**Step 3. Rank by the product.**

**Step 4. Do not compute freshness yourself.** Rates live for quarters, bridge
limits for years. By how much a document has been discounted depends on the
question, and the model is what knows it.

---

An honesty check: **substitute one for `freshness` and see what is found.** If
the answer did not change, the date plays no part in your ranking and you have
merely guessed right so far.
