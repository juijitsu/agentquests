# Red team · The prompt is clean

You have the surface of inputs from the first level and the notes that work
from the second. Now you have gone down to the level of calls and taken apart
one agent call on load L-4471: six arguments.

You checked the ones the model wrote itself and found one dangerous: the text
of the notification was assembled out of the shipper's note. The rest the model
did not write; the code filled them in, and the prompt does not go through
them.

```
python engine/check.py content/en/05-red-team/03-borrowed-argument/starter/novice/agent.py
```

Look at the line about what was missed. There are two. The code filled in both:
one took the address from the consignee's contact, the other the number from
the broker's document. Both fields are filled in from outside, without your
password.

The prompt was clean. Those values never went through it.

**Find the arguments whose value comes from an input controlled from
outside.**

## Done when

- every argument of the call has been traced;
- every argument from the surface made it into the report;
- there are no extra arguments in the report;
- the number of calls claimed matches the number made.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | selection by the author of the string, with the sign named in a `TODO` |
| `starter/advanced/` | selection by the author of the string, with no hint |
| `starter/pro/` | the contract and the definition of an argument from the surface |

## If you get stuck

The question is not "who wrote the value" but "whose hands typed what ended up
in it". The path through the code is shorter than the path through the model,
and it goes through none of the prompt's defences.
