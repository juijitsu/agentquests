# Theory · Not everything goes through the model

The previous level taught you to look at behaviour instead of text. An agent's
behaviour is made of tool calls, and a call is made of arguments. Here we go
down to that level: **which arguments does the attacker control.**

## Where argument values come from

The agent calls `send_sheet(to="...")`. Somebody put exactly that string into
`to`. There are two possibilities.

Either the model wrote it: it read the context, decided who to send to, and
produced an address. Or the code filled it in: it took a field from the load
record and passed it into the argument as is, without asking the model.

Both calls look identical. One line in the log, no visible difference.

## The mistake that closes off half the surface

The red team knows an injection is about the prompt. So, it reasons, the
dangerous arguments are the ones the model wrote itself: those you can reach
with text.

The arguments the code filled in get skipped. The logic looks airtight: the
prompt does not go through them, you cannot push on them with text, there is no
injection to be found there.

The logic is right. The conclusion is not.

## Why the code path is worse than the model path

A value the code copied out of a field came **from that same field.** If the
consignee fills that field in through a form on the portal, then the consignee
sets the content of the argument. The model simply does not take part.

And that is worse, not better. Everything used to defend a prompt — role
markers, instructions not to carry out fetched text, checks for suspicious
phrasing — works on the path through the model. An argument the code filled in
goes through none of those defences. It lands in the call directly.

Hence the rule: **an argument is dangerous because of where its value came
from, not because of who wrote it.** The author of the string does not matter.
What matters is whose hands typed what ended up in it.

## What this looks like in real life

`send_sheet(to=...)` takes the address from the consignee's contact. The
consignee fills that in. The rate sheet goes wherever the person who was never
supposed to see it asked for it to go. Not one word of the attack was in the
prompt.

`file_customs(doc_no=...)` takes the number from the broker's document. The
broker is not your employee, and that field is filled in without your password.

The red team checked the prompt, found nothing, and was right: there was
nothing in the prompt.

## The boundaries

This is still an inventory, not a fix. The result of the level is a list of
arguments whose values arrive from outside. What to do about them is the
defence's decision, and the decisions differ: an argument from the model can be
fixed with an instruction, an argument from the code cannot be fixed with an
instruction at all.
