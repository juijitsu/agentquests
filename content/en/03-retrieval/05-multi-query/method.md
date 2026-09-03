# Method · Split, search, merge

**Step 1. Split the question.**

```python
for part in model.split(question):
```

Splitting is the model's work: only something that understands meaning can tell
that "and" here joins two different questions rather than one clarifying the
other.

**Step 2. Search for every part separately.**

```python
run_tool("search", {"query": part})
```

Separately is the point. Gluing the parts back into one string and searching for
that is exactly where you started.

**Step 3. Merge, dropping repeats by id.**

```python
if doc["id"] not in seen:
    seen.add(doc["id"])
    found.append(doc)
```

**Step 4. Do not trim the union back to one selection's size.** The top-2 is set
for a single query. Two queries legitimately bring up to four documents, and
cutting them back to two hands you the original problem again.

---

An honesty check: **count how many times you called the search.** If it is once
and the question is compound, half the answer was never searched for.
