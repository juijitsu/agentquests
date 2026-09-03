# Method · One pass per half

The whole search engine is a loop over sub-questions, and inside it four steps in
strict order.

**Split the question.**

```python
for part in model.split(question):
```

**Narrow, if there is something to narrow by.**

```python
token = model.identifier(part)
pool = run_tool("exact", {"token": token}) if token else DOCS
```

Not every half has an identifier: the bridge question has none, and there the
corpus stays whole.

**Rank by the product.**

```python
key=lambda d: model.similarity(part, d["text"]) * model.freshness(d)
```

**Check the floor against the best one and leave if it falls short.**

```python
if best < THRESHOLD:
    selection.append(model.say_missing(part))
    continue
```

**Build the selection, skipping repeats.**

```python
if any(model.same_fact(doc["text"], p["text"]) for p in picked):
    continue
```

---

An honesty check: **remove each of the five steps in turn and run it.** If the
answer does not change, that step does nothing in your search engine — and on
other data you will get the very error it was there to prevent.
