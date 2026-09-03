# Theory · An error is a message

On the previous level you learned not to take the process down. Now a finer
question: **who is the refusal addressed to**.

Refusals come in two kinds, and mixing them up is expensive.

**A refusal for the human.** Out of step budget, provider unreachable, no
permissions. The agent can do nothing about it — a person has to step in.

**A refusal for the model.** A wrong argument value, a typo in a name, the wrong
format. The model can fix this — if it finds out.

The difference is practical. The first refusal goes out and ends the work. The
second goes back **into the loop** and the work continues.

## What happens to an exception

A tool raised `ValueError`. Three scenarios follow.

**Not caught.** The process died, the user sees a stack trace. That is level 05.

**Caught and returned to the human.** The process is alive, the user got a polite
"could not do it". It looks decent — and it is still wrong: the agent gave up
where one extra step would have fixed it.

**Caught and returned to the model.** The error text is put into `messages` with
the role `tool` — like any ordinary call result. On the next iteration the model
reads it and tries again, correctly this time.

Only the third option makes an agent an agent.

## Why the error text matters more than the error

The model will correct itself only if it understands what is wrong. A message
saying "invalid argument" helps nobody. A message saying

> crossing 'Loredo' does not exist. Available: Laredo, El Paso, Otay Mesa

carries both the diagnosis and the list to choose from. **List the allowed values
in the error text** — it is the cheapest thing you can do for self-correction.
