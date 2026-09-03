# Method · Take inventory of the inputs

**Step 1. Get the list of inputs from the agent itself.** Not from memory, and
not from code you read a month ago:

```python
inputs = run_tool("inputs", {})
```

Memory fails exactly where an input was added recently — and recent inputs are
the least checked ones.

**Step 2. Ask about every one of them who controls it.**

```python
model.who_controls(item["id"])
```

About **every** one, not about the suspicious ones. The suspicious ones will be
the wrong ones: you suspect what you remember, and you remember what you have
worked with.

**Step 3. Keep the ones from outside.** That is the surface. An input your own
employee is responsible for does not belong in it — not because it is safe, but
because it is a different job and a different threat.

**Step 4. Do not defend anything at this step.** An inventory of inputs fixes
nothing, and it should not. Its result is a list of places worth pushing on;
the pushing comes later.

---

An honesty check: **take your list and, for every input on it, name the person
who writes there.** If for some input the answer comes out as "well, customers"
instead of a name, that input is from outside, and you have just found what you
were looking for.
