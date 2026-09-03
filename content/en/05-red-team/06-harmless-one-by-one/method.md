# Method · The verdict at the moment it runs

**Step 1. Take the queue.**

```python
steps = run_tool("list_batch", {"batch": BATCH_ID})
```

Its order is the execution order. That matters more than any field in it.

**Step 2. Take the verdict on its own.**

```python
alone = {s["id"]: model.check(s["id"])["allowed"] for s in steps}
```

`check` changes nothing, so all ten can be asked in a row against the untouched
record.

**Step 3. Take the verdict from inside.**

```python
for s in steps:
    inside[s["id"]] = model.check(s["id"])["allowed"]
    model.run_step(s["id"])
```

The question sits between the earlier steps' writes and this step's own run.
The guard has no other moment.

**Step 4. The report is the difference in one direction.**

```python
inside[i] and not alone[i]
```

Refused by itself, permitted in the chain. The opposite difference is noise: a
step the batch broke is not a finding.

**Step 5. Do not take a second snapshot.** The record after the batch answers a
question nobody asked.

---

An honesty check: **for every step in your report, name the step that unlocked
it and the field that step wrote.** If there is nothing to name, you caught a
coincidence, not a chain.
