# Method · A threshold and an honest refusal

**Step 1. Find the best one as before.** Ranking has not gone anywhere and is
still needed: to decide whether the first one is good enough, you first have to
identify it.

**Step 2. Compare its similarity against the floor.**

```python
if model.similarity(question, best["text"]) < THRESHOLD:
```

What is compared is the **absolute** value, not the gap to second place. The gap
is useful too, but it is relative again: two equally bad documents give a zero
gap exactly as two equally good ones do.

**Step 3. Refuse on the substance.**

```python
return model.say_missing(question), 1
```

The refusal names the subject of the question, because "not found" does not say
what exactly is missing.

**Step 4. Check that the threshold did not eat the working case.** Too high a
threshold turns the search into a permanent "not found". Run both questions — the
one with an answer and the one without.

---

An honesty check: **think of a question whose answer is certainly in the corpus
and one that certainly is not.** If your system answers both the same way — no
matter how — it has no threshold.
