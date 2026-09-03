# Method · Write after the fact

**Step 1. Find the irreversible action.** There are usually one or two in a loop:
the one after which the world has changed. Here it is `book` — a booking costs
money.

**Step 2. Find the point where the result is known.** That is the line right
after the tool returns. Before it the action has not happened; after it, it has
happened and is confirmed:

```python
result = run_tool(call.name, call.arguments)
messages.append({"role": "tool", "content": result})
DONE.append(call.arguments["leg"])
```

**Step 3. Write outside, not into the history.** `messages` is not state. Writing
into it survives neither a restart nor the compaction from level 03.

**Step 4. Write nothing about the future.** The state must hold no plans and no
intentions — only facts that have occurred. A plan can be rebuilt; a paid booking
cannot be returned.

---

An honesty check: **close your eyes to the code and ask what would be left after
a `kill -9` on any line.** If the answer is "depends which one", the state is
written in the wrong place.
