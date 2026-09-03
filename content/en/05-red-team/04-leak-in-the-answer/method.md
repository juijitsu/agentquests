# Method · Look at the output, not at the log

**Step 1. Take the shift's requests.**

```python
requests = run_tool("requests", {})
```

**Step 2. For each, take the facts that ended up in the answer.**

```python
model.facts(r["id"])
```

Not the text of the answer, but the facts it was assembled from: each one has
an owner.

**Step 3. Compare the owner with the asker.**

```python
any(f["owner"] != CALLER for f in facts)
```

One foreign fact is already a leak. An answer does not get safer because nine
of the facts in it are the asker's own.

**Step 4. Do not open the call log.** `model.calls` exists, and what it lies
about is not the data but the question: it answers about the agent's rights. A
refusal in it means the data did not go out, which is the opposite of what you
are looking for.

---

An honesty check: **take a request you did not flag and name the owner of every
fact in its answer.** If the owner of some fact takes a moment to name, you
have found another leak.
