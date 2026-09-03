# Task · Say hello by name

## What to do

The file `agent.py` holds one function:

```python
def solve(name: str) -> str:
    return "Hello!"
```

A name is passed to it, and it has to return a greeting **with that name in
it**.

```
solve("Maria")  ->  "Hello, Maria!"
solve("John")   ->  "Hello, John!"
```

The answer is compared character by character: the word Hello, a comma, a
**space**, the name, an exclamation mark. One space too many or too few is a
different answer, and the check notices.

**Return the greeting with the name in it.**

## Why the starter does not pass

It returns `"Hello!"` — text with no name in it. That is the same for all five,
so it matches none of them. The name has to be taken from the parameter `name`
and put into the answer.

## Done when

- the function **returns** text instead of printing it;
- all five names matched.

The task shows two names; the check runs five. Writing the answer out by hand
will not work: you cannot see the other three, and they are different.

## What not to do in this task

- **Do not rename `solve`** — the check looks for the function by that name and
  will not find another.
- **Do not write a person's name into the text.** `return "Hello, Maria!"` runs
  and even passes the first name, but fails the other four.
- **Do not put `name` in quotes.** `"name"` is four letters, not a value.
- **Do not write `print`.** It will look right on screen, but nothing comes
  back, and the first verdict line will say "returned text: no".
- **Do not delete the four spaces** at the start of the line: Python uses them
  to know the line is inside the function.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | the starter and a `TODO` spelling out what to type |
| `starter/advanced/` | the same starter and an example call, no instructions |
| `starter/pro/` | the function contract only, empty body |

## If you get stuck

The answer is assembled from three pieces, joined with a plus:

```
"Hello, "   +   name   +   "!"
   text        label       text
```

Text goes in quotes, the label does not. The space after the comma sits
**inside** the quotes, or the words run together.

If it really will not come — there is a star in the corner of the solve page.
It looks at your last run and hints from it: it names the condition that did
not line up and what to do about it.
