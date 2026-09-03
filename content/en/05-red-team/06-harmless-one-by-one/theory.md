# Theory · The guard reads a state, and the state moves

For five levels you asked about a property of a single call: who controls an
input, where an argument's value came from, whose rights a tool checked, what a
rule's wording covers. All five are computed once and do not depend on order.

Here state appears for the first time. And the property you are testing —
permitted or refused — stops being a property of the step. It becomes a
property of **the step and the moment.**

## What the nightly batch does

At midnight a maintenance queue runs over the carrier record: upload the
insurance scan, verify against it, release the credit hold, tender the load,
close the batch. Every step has an access check, and it is not for show: it
reads fields of that same record and it does refuse.

It reads them at the moment the step runs. Not earlier and not later.

## The mistake that looks like an audit

The red team takes two snapshots: the record before the batch and the record
after. It compares verdicts. That is exactly what any after-the-fact review
does, and it sounds unimpeachable.

The last step of the batch puts the defaults back. The carrier is provisional
again, the hold is on again, the limit is zero again.

So the steps the whole thing was about are refused again by the time of the
second snapshot. They never reach the report. And the load has been tendered.

## Both halves of the error

A snapshot taken after the batch lies twice.

It **loses** the steps that fired in the middle and left no trace. Releasing
the credit hold was permitted because two steps earlier the carrier had become
standard. Then it was put back to provisional, and the same guard refuses
again.

It **adds** steps that are permitted at the end but were not when they ran. A
dedicated lane requires verified insurance. By the end of the batch the
insurance is verified, but that step stood third, two steps before the
verification, and it was refused.

Permitted later is not permitted then.

## What it ends in

Before the batch the record says: provisional carrier, hold on. After the batch
it says the same. All that changed is that an insurance scan arrived and a
verification was logged.

And a hazmat load sits on a provisional carrier.

## What is not a finding

The batch contains two refusals. Both are fine: archiving the paperwork did not
go through because the tier had already changed, and the exemption did not go
through because the archiving did not. A refusal means nothing happened. That
was level 04's lesson, and it still holds here.

## The boundaries

This is a report, not a fix. The fix is to stop the guard reading mutable
state: either rights are computed once for the whole batch, or a step declares
which state it depends on. That choice is not yours to make.
