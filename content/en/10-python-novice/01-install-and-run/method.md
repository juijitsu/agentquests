# Method · How to solve it, step by step

No explanations here, only actions. The theory is above if something is
unclear — go back to it.

---

## Step 1. Open the solver

The **"Solve this level"** button at the bottom of the page. A terminal opens
with the starter already in it — you are not writing from a blank file.

To the left of the Run button there are three difficulties. Start with
**"Novice"**: the code there has a `TODO` saying exactly what to type.

---

## Step 2. Look at what is already there

The starter holds this:

```python
def solve(name: str) -> str:
    # TODO: ...
    return "Hello!"
```

The function works. It runs, it breaks nothing, and it returns text. The text
is simply the wrong one: there is no name in it.

See for yourself — press **Run** right now, without changing anything. You
will get:

```
✓ returned text: yes
✗ names matched: 0 of 5
✗ first difference: on the name "Maria"
    expected: Hello, Maria!
    got:      Hello!
                   ^
```

The first line is green: the type is right, text came back. The second is red:
not one name matched. The third shows the first difference, with an arrow at
the place the strings part.

**That is how to start any level: run the starter as it is.** It will tell you
what is missing.

---

## Step 3. Replace the return line

You need to turn

```python
    return "Hello!"
```

into

```python
    return "Hello, " + name + "!"
```

The answer is built from three pieces, joined with a plus:

- `"Hello, "` — text, so it goes in quotes. The space after the comma sits
  **inside** the quotes: it is part of the text, not spacing between code.
- `name` — **without quotes**. It is a label, not text. In quotes it would
  turn into four letters.
- `"!"` — text again.

The whole line:

```python
    return "Hello, " + name + "!"
```

The four spaces at the start are mandatory. They are already in the starter —
do not delete them.

---

## Step 4. Run it

The **Run** button, or `Ctrl+Enter`.

If it is right:

```
✓ returned text: yes
✓ names matched: 5 of 5
✓ first difference: all matched

PASS  the next level is open
```

---

## Step 5. If it does not match

The verdict always says what is wrong. Three typical cases:

**The strings are nearly identical but did not match.** Look at the arrow. It
stands exactly under the first character that differs. Most often that is a
missing or extra space after the comma.

```
expected: Hello, Maria!
got:      Hello,Maria!
                ^ a space is missing here
```

**The same string for every name.** That means the name is written into the
text and the label `name` is unused. Go back to step 3.

**An error name instead of a verdict.** The program did not run. Under the
error there is an explanation in plain words: what happened and what to fix.
The common ones:

- `IndentationError` — the four spaces at the start of the line were deleted;
- `SyntaxError` — a quote or bracket was left unclosed;
- `NameError` — text was written without quotes.

---

## Step 6. Check that you understood

Optional, but useful. Press **"Paste the solution"**, look at it, then press
**"Reset to starter"** and type the same thing yourself without peeking.

If it comes out right first time, the level has landed. If not, you have just
found the part worth rereading.

---

## Running it on your own machine

Only needed if you installed Python locally. Download the repository and, from
its root, run:

```
python engine/check.py content/en/10-python-novice/01-install-and-run/starter/novice/agent.py
```

That is exactly what the button on the page does: the same engine, the same
verdict.
