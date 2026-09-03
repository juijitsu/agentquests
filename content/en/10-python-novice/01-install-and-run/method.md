# Method · Edit, run, read

**Step 1. Open the solver.** The "Solve this level" button opens a page with a
terminal. The starter is already in it; you are not writing from a blank file.

**Step 2. Edit the body of the function.** Everything below the
`def solve(name):` line and indented to the right is the body. The indent is
not decoration: Python uses it to know where the function begins and ends. Four
spaces, not a tab.

**Step 3. Run it.** The Run button, or `Ctrl+Enter`.

**Step 4. Read the verdict.** Three lines:

```
returned text: yes
names matched: 0 of 5
first difference: on the name "Maria"
    expected: Hello, Maria!
    got:      Hello!, Maria!
                   ^
```

The first line is about the type: if it says no, the function returned
something that is not text — most often because it has `print` where `return`
should be, and then nothing comes back at all.

The second says how many names lined up. The third shows the first mismatch:
the two strings one under the other, with an arrow under the first place
they part. Two similar strings side by side cannot be compared by eye, so
the place is named outright.

**Step 5. If the program crashed.** There is no verdict then; instead you get
the name of the error and an explanation in plain words. The most common ones
on this level: an unclosed quote, a missing colon after `def`, a body that was
not indented.

## If you want to run it on your own machine

Download the repository and, from its root, run:

```
python engine/check.py content/en/10-python-novice/01-install-and-run/starter/novice/agent.py
```

That is exactly what the button on the page does.
