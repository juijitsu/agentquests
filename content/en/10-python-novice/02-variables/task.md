# Task · Add the deadhead

## What to do

The dispatch board sends the loaded miles as text: digits only, no spaces and
no signs. Every load also carries the empty run to the pickup — the deadhead,
always 60 miles.

Return one line: the miles exactly as they came in, then ` + 60 = `, then the
sum.

```
solve("1450")  ->  "1450 + 60 = 1510"
solve("300")   ->  "300 + 60 = 360"
```

The spaces around the plus and the equals are single. The whole answer is text.

**Note this:** the miles appear twice in the answer. On the left, exactly as
they arrived. On the right, inside the sum. That is the whole task.

## Why the starter does not pass

It does `miles + "60"`. Both pieces are text, so the plus glues them: the
result is `"145060"` instead of `1510`. The program does not crash and the
answer is wrong.

## Done when

- the function returns text instead of printing it;
- all six loads matched.

The task shows two; the check runs six. Among the hidden ones are cases where
the sum is longer than the miles and where the input digit does not appear in
the sum at all — fitting an answer to the examples will not work.

## What not to do in this task

- **Do not put quotes around the 60** to make the `TypeError` go away. The
  error will go and the answer will quietly become wrong — that is the starter.
- **Do not turn the whole answer into a number:** it is not only digits.
- **Do not touch `miles` on the left:** it has to stay exactly as it arrived.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | the starter and a `TODO` with the calls you need |
| `starter/advanced/` | the starter and one line about what is wrong |
| `starter/pro/` | the function contract only |

## If you get stuck

A plus does different things depending on what is on either side: two pieces of
text it glues, two numbers it adds. So before adding, both sides have to become
numbers — `int(text)` — and before gluing back into the answer, text again —
`str(number)`.
