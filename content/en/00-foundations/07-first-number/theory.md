# Theory · The first number

You have been testing the agent like this: asked a question, looked at the
answer, liked the answer. That is not a test. That is an impression.

One good run proves nothing — you asked a question whose answer you already knew,
and on that one the agent works. The other ninety questions you never asked.

**Until there is a score, arguing about quality is pointless.** "It got better"
with no number is an argument about taste, and it is won by whoever is louder.

## What a case is

A pair: what to ask, and what must appear in the answer.

```python
("How much does it cost to haul a 12-ton load?", "1080")
```

The expectation is written as a substring, not as the full text. The wording of
an answer can change; the fact cannot. The fact is what you check.

## A set has to discriminate

The main property of a good set is that it is **red on a broken agent and green
on a healthy one**. Two kinds of sloppiness look like work and are not:

**Cases that always pass.** You wrote five questions about the same thing, got
five out of five and decided everything was fine. Such a set catches nothing.

**Cases that always fail.** The expectation is phrased so it can never match. The
number is low, the alarm is permanent, the value is zero.

There is only one way to check a set: **run it against a knowingly broken agent
and a knowingly healthy one.** If the result is the same, the set measures
nothing.

## Where cases come from

Not from your head. From the complaints log, from support tickets, from what was
actually asked. Invented cases cover what you already thought of — and what
breaks is always what you did not.
