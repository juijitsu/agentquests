# The finale of Foundations

There is no new theory here. You already know everything you need — the task is
to apply it to code you did not write.

## How someone else's code differs from your own

In your own you remember the intent. In someone else's you do not, and that
changes the order of work.

**In your own code you look for where you made a mistake.** In someone else's you
first work out what the author was even trying to do, and only then where it
stopped working.

Hence the rule: **do not read someone else's agent top to bottom.** A
seventy-line file reads in five minutes and gives you nothing. It is far quicker
to run it, get a list of failures, and go from symptom to line.

## What you already have

Six lessons are six symptoms you now recognise:

| Symptom | Where to look |
|---|---|
| identical calls in a row | the tool result never reaches the history |
| the agent reported, nothing happened | tools are not run, only text is parsed |
| a confident wrong answer | part of the history never reaches the model |
| the wrong tool was called | the description does not let it be recognised |
| a stack trace escaping | protection fired but was shaped as an incident |
| the agent politely gave up | the error went to the human instead of the model |

Those six rows are worth more than the ability to write agents from scratch. You
will write rarely; you will read other people's code constantly.
