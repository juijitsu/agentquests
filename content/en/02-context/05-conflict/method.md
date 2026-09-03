# Method · Accumulate, do not overwrite

**Step 1. Find the place where many turn into one.** Usually a dict assignment or
a dict comprehension. The mark: a list goes in, a mapping comes out, and nobody
asked what to do about repeated keys.

**Step 2. Replace the write with an append.**

```python
merged.setdefault(fact["field"], []).append((fact["source"], fact["value"]))
```

`setdefault` creates the list the first time a field appears and returns the
existing one afterwards. One line instead of three with a presence check.

**Step 3. Put the source next to the value.** A reading with no source settles
nothing: the discrepancy is visible and there is nobody to call.

**Step 4. Do not decide for the model.** The temptation to pick the "more
trustworthy" document is strong, and sometimes a rule really exists — a weigh
ticket outranks a bill of lading. But that is a domain rule, and it lives in the
task, not in the context assembler. The assembler has to convey both readings;
which one outranks the other is decided higher up.

---

An honesty check: **count the facts going in and the readings coming out.** If
the second is smaller than the first, you threw something away — and did not
notice you were choosing.
