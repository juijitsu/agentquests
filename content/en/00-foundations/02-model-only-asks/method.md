# Method · The order of checks inside the loop

This level's bug lives in a single line — in **what order** the loop takes apart
the model's answer.

An answer can contain both text and a request to call a tool **at the same
time**. Check the text first and return immediately, and the request stays
unfulfilled while a report of work never done goes out the door.

The right order:

**Step 1. Tools first.** There are `tool_calls` — run them all, put the results
back into `messages`, go to the next iteration. The text is ignored here: it is
intermediate.

**Step 2. Text only when there are no requests left.** An empty `tool_calls`
means the model is finished. Now its text is the answer.

```python
if response.tool_calls:          # this first
    ...run them and continue...
return response.text, step       # and only then this
```

**Step 3. Check by consequences.** The only way to be sure an action happened is
the trace it leaves: a row in a journal, a file on disk, a record in a database.
The agent's words are not evidence.
