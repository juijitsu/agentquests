# First run · Say hello

The file is called `agent.py` — that is how the check finds it throughout the
course, so leave the name alone. Inside there is one function:

```python
def solve(name: str) -> str:
    ...
```

A name is passed to it, and it has to return a greeting.

```
solve("Maria")  ->  "Hello, Maria!"
solve("John")   ->  "Hello, John!"
```

Note how exact this is: the word Hello, a comma, a **space**, the name, an
exclamation mark. One space too many or too few is a different answer.

The starter returns a greeting with no name in it, so it matches none of them.

**Return the greeting with the name in it.**

## Done when

- the function returns text instead of printing it;
- all five names matched.

The task shows two names; the check runs five. Writing the answer out by hand
will not work: you cannot see the other three.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | the starter and a `TODO` spelling out what to type |
| `starter/advanced/` | the starter and an example call |
| `starter/pro/` | the function contract and nothing else |

## If you get stuck

Text in quotes is joined with a plus: `"a" + "b"` gives `"ab"`. The name is in
the variable `name`, and it needs no quotes around it — it is already text. Put
three pieces together: what comes before the name, the name, and what comes
after.
