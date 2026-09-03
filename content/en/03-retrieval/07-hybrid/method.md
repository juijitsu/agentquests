# Method · Narrow with exact, choose with meaning

**Step 1. Pull the identifier out of the question.**

```python
token = model.identifier(question)
```

From the model, specifically: you cannot tell a waybill number from a tonnage by
the look of the string, both are made of digits.

**Step 2. Narrow the corpus with an exact match.**

```python
same_number = run_tool("exact", {"token": token})
```

What is searched for is the **identifier**, not the whole question. An exact
search over the whole question returns what it did before: matches on stray
words.

**Step 3. Choose by meaning within the narrowed set.**

```python
best = max(same_number, key=lambda d: model.similarity(question, d["text"]))
```

**Step 4. Do not swap the steps.** Meaning first and the number second means
choosing among three identical documents and hoping for the list order.

---

An honesty check: **remove the number from the question and see what is found.**
If the result is the same, the number plays no part in your search, and you will
get the neighbouring waybill wrong.
