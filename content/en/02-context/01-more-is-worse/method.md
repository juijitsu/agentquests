# Method · Select against the question

**Step 1. State what the question is about.** Not "what documents exist" but
"which topic settles this question". The model judges that:

```python
topic = model.topic(question)
```

**Step 2. Take only what bears on it.** The index returns the fitting papers as a
list:

```python
blocks = run_tool("about", {"topic": topic}).split(" | ")
```

**Step 3. Send those into the window, not the whole folder.** Anything you add on
top pushes the needed one deeper.

**Step 4. Check by counting.** If there are more blocks than the model reads in
full, you are hiding the answer in the middle again — and it does not matter that
formally it was passed.

---

An honesty check: **compare the length of what you sent with the length of what
actually settles the question.** The difference between them is what you buried
the answer under.
