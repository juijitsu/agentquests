# Theory · Three ways to break

Agents break in ways that look varied and are the same underneath. There are
exactly three, and knowing their symptoms saves hours.

## Looping

The model asks for the same tool again and again. Usually because the result does
not satisfy it: the tool returned empty, an error, or a useless "please retry".

**Symptom in the log:** identical call lines in a row, arguments unchanged.

**Cost:** without a limiter the loop never ends and quietly burns money. This is
the only one of the three that is dangerous on its own.

## Context overflow

The `messages` list grows on every iteration. On a long task it hits the window
size and the call fails.

**Symptom:** a length error from the provider, and not right away but after N
turns. It never reproduces on short checks.

## Invented arguments

The model calls a tool with a value that does not exist: a nonexistent number, a
typo in a name, a field of the wrong type.

**Symptom:** an exception inside your tool, not in the agent code.

---

## Why you cannot see them in advance

None of the three shows up on the happy path. You test the agent with a question
whose answer you know, everything works, and you are sure it is ready.

**Not one of the three reproduces on a successful scenario.** They are waiting
for the first real user.

## What they have in common

All three turn into an incident only if the code is not ready for them. Looping
is cured by a counter, overflow by collapsing history, invented arguments by a
check before the call.

And all three share a property that is the subject of this task: **running out of
protection is a normal outcome, not a crash.** The limiter fired — that means it
did its job. The user should get an explanation, not a stack trace.
