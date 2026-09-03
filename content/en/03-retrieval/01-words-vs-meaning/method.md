# Method · Closeness instead of matching

**Step 1. Translate the question and the documents into a shared space.** On this
level through `model.embed`, in real life through an embedding model. What
matters is that **the query and the documents are translated the same way**: only
comparable things can be compared.

**Step 2. Compute the closeness to every document.**

```python
model.similarity(question, doc["text"])
```

**Step 3. Take the best one.**

```python
best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))
```

`max` with a key walks the corpus once and needs no sorting: when you want one
document, there is no reason to sort the whole list.

**Step 4. Do not mix in words "just in case".** The temptation to add both
methods together is strong, and on later levels we come back to it deliberately.
Right now mixing would only hide whether the meaning search works.

---

An honesty check: **rewrite the question in different words, keeping the
meaning.** If the document found changes, you are still searching by spelling.
