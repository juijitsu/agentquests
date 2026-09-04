# Task · The whiteboard label

## What to do

The dispatcher writes a run label on the board by hand, and it is then typed
into the system exactly as it stands. It arrives dirty: stray spaces and
newlines at the edges, mixed case. The label ends with a two-digit run number.

Build a short code out of the label by three rules:

1. remove the whitespace **at the edges** — touch nothing inside;
2. put it in capitals;
3. take the first three characters and the last two, glued together.

```
solve("  dallas run 47 ")  ->  "DAL47"
solve("memphis run 08")    ->  "MEM08"
solve("  Reno Run 12")     ->  "REN12"
solve("OMAHA RUN 33")      ->  "OMA33"
```

The first three characters give the city, the last two the run number.

**Note this:** the rule about the first three characters means literally the
first three characters of the cleaned string. Among the hidden labels there is
one whose first word is shorter than three letters — then a space lands in the
code too. That is the rule, not a bug.

## Why the starter does not pass

It calls `text.strip()` and `text.upper()` but puts the result nowhere.
Strings in Python do not change: a method returns a new string and the old one
stays as it was. So what gets cut is still the dirty label.

The starter matches on exactly one label out of ten — the one that arrived
clean and in capitals already.

## Done when

- the function returns text instead of printing it;
- all ten labels matched.

The task shows four; the check runs ten. Among the hidden ones are labels with
newlines at the edges and labels with spaces only on the right — fitting an
answer to the examples will not work.

## What not to do in this task

- **Do not trim with a slice** like `text[2:-1]`: different labels carry a
  different number of spaces at the edges.
- **Do not remove the spaces inside the label.** Only the edges are to go.
- **Do not cut `text`** after cleaning — cut the name the cleaning went into.
- **Do not write a method without brackets:** `text.strip` is the method
  itself, not a string.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | the starter and a `TODO` with the lines you need |
| `starter/advanced/` | the starter and one line about what is wrong |
| `starter/pro/` | the function contract only |

## If you get stuck

A string method is not an order, it is a question: it does not change the
string, it answers with a new one. So after every call there has to be a name
the answer went into — and that is what gets cut.
