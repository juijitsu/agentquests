# Method · Rebuild, then judge

**Step 1. Ask for each candidate's neighbours.** The tool returns the chunks of
the same document in order:

```python
run_tool("neighbours", {"id": chunk["id"]})
```

**Step 2. Join them into one text.** Order matters: "after that" only means
something after the sentence it refers to.

```python
text = " ".join(c["text"] for c in neighbours)
```

**Step 3. Run the fitness check on the joined text.** That is the key change from
the previous level: what you judge is the whole, not the chunk.

**Step 4. Compute similarity on the whole too.** The joined text is closer to the
question than either of its halves — because it finally holds both the bridge and
the mass.

---

An honesty check: **look at what you hand to the fitness check.** If it is
`chunk["text"]`, you are still judging a chunk. If it is the joined text, you are
judging a fact.
