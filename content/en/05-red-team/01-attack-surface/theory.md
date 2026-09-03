# Theory · The field you remembered first

For five tracks you have been building an agent. This track is about breaking
one, and the one you break has to be yours, before somebody else's turn comes.

None of it starts with an attack. It starts with a question: **where can you
push at all.**

## What an attack surface is

The agent does not read one field. Into its window come the dispatcher's
question, the shipper's note, the consignee's contact, the company rate sheet,
the driver's marks, the customs broker's document.

Six inputs. The model sees all six the same way: as text.

But different people control them. Your department writes the rate sheet, your
driver leaves the marks, your dispatcher types the question. The shipper's note
is filled in by the shipper, a person from outside your company, through a form
on the portal, and nobody on your side ever reads that field.

**The attack surface is the inputs whose content is set by somebody outside.**

## Why the first field turns out to be the wrong one

Ask anyone where to attack a chat agent and you will hear: the input box. That
is where people type "ignore previous instructions", everybody has seen it.

Look at this agent. The input box is the dispatcher's question. The dispatcher
sits in the next room, with a badge and an employment contract. To write
anything there, an attacker has to become your employee first.

The shipper's note is filled in without a single password, by any customer, in
two minutes.

Hence a rule that is unpleasant precisely because it is so simple: **the input
you remembered first is usually the one the attacker controls least.** You
remembered it because it is in plain sight; it is in plain sight because your
own people work through it.

## How this ends in practice

The red team checks the input box, finds nothing, and writes in the report:
no injections found. A month later a shipper writes a sentence in the note that
is not addressed to a human, and the agent carries it out.

The report was honest. It just answered the wrong question: what got checked was
not the attack surface but a habit.

## How to tell who controls an input

One question: **can the content of this field appear there without anyone from
your company touching it?**

Not "can an outsider influence it" — anything can be influenced, the rate sheet
included, if you talk the sales department into it. The question is whether the
text goes straight in, with no person responsible for it in between.

If it does, the input is from outside and it belongs in the surface. If it does
not, it is not in the surface, and there is no reason to spend red team time
on it.

## The boundaries of this track

Everything that happens here happens to your agent, in your environment, before
release. A red team exists to find the hole before somebody walks into it: its
work ends with a report, which the defence then fixes.

Level 07 of the Context track was building that defence — it marked fetched
text with a role so it would not read as an order. Here you stand on the other
side and see what the defence covers and what it does not.
