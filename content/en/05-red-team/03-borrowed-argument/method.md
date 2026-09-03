# Method · Trace the value back to an input

**Step 1. Take the arguments from the call, not from the code.**

```python
args = run_tool("calls", {})
```

The code shows what is supposed to be filled in. The call shows what was.

**Step 2. Ask about every argument where its value came from.**

```python
model.trace(a["id"])
```

The answer is the input the value came from, and the path it came by.

**Step 3. Look at the source, ignore the path.**

```python
model.trace(a["id"])["source"] in SURFACE
```

`SURFACE` is the result of the first level: the inputs controlled from outside.
The path will be useful later, to the defence: it says what to fix the argument
with. It does not say whether the argument is dangerous.

**Step 4. Do not fix anything.** An inventory of arguments closes none of them.

---

An honesty check: **take an argument that did not make it into the report and
name the employee who typed its value.** If there is no name, only "well, it
comes in with the load", you did not trace it all the way.
