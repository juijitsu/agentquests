# Method · Two steps and their order

**Step 1. Select the fit ones.** The check runs over every candidate, not over
one:

```python
fit = [d for d in DOCS if model.answers(question, d)]
```

**Step 2. Among them take the most similar.**

```python
best = max(fit, key=lambda d: model.similarity(question, d["text"]))
```

Similarity has not gone anywhere and is still needed: there may be several fit
documents, and choosing among them goes by closeness to the question. On this
level there are two — the price line for the lane you want and one for another
lane.

**Step 3. Do not swap the steps.** Taking the most similar first and then
checking it for fitness means ending up with nothing when the check fails.
Filtering narrows the field; similarity picks the best within it.

**Step 4. Do not judge fitness yourself.** What counts as an answer depends on
the question: "how much" wants a number, "when" a date, "may we" a yes or no.
That is the model's work.

---

An honesty check: **remove the price line from the corpus and run it.** A good
search will say there is no answer. A bad one will confidently return the policy
— which is exactly what you are fixing now.
