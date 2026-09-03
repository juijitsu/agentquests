# Method · A signature on every line

**Step 1. Select as on the previous level.** Nothing changes:

```python
lines = run_tool("about", {"topic": model.topic(question)}).split(" | ")
```

**Step 2. Ask for the source of every line.** The index knows where each one came
from:

```python
who = run_tool("source", {"line": line})
```

The line is passed exactly as `about` returned it. A signature you have already
glued on makes the line unrecognisable to the index.

**Step 3. Join the signature to the line.** One simple format:

```python
f"{who}: {line}"
```

It matters that the signature stands **before** the content, not after: the model
looks for an anchor left to right and attaches the fact to the last name it saw.

**Step 4. Add nothing on top.** The number of blocks must not grow: signing
changes the lines, not how many there are.

---

An honesty check: **cover the question with your hand and read one block on its
own.** If you cannot tell who it refers to, you sent hearsay.
