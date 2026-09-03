# Theory · When a plan stops being a plan

This is the border between an agent and a script, and it does not run where
people usually think.

A script performs steps. An agent performs steps **and notices when the steps
stopped leading to the goal**. Everything else is detail.

## What is really happening

A tool returned "road closed". To the loop that is an ordinary result: a string
that lands in the history next to the others. Nothing crashed, no limiter fired,
the next iteration starts as if nothing happened.

The model will see the next item in the plan and drive there. The route will be
covered — with a hole in the middle. The agent will report a delivery.

**A failure of this kind leaves no trace.** No exception, no error in the log.
Only a mismatch between what was planned and what happened — and nobody asked for
those to be compared.

## Who does what

It is easy to err in both directions here, so let us separate them plainly.

**Noticing the plan is broken is your code's job.** This is not magic and not the
model's work. The tool result arrives in your loop, and the decision "this result
invalidates the plan" is made right there. No wording of a prompt replaces a
check.

**Inventing the way around is the model's job.** This is where being an agent
begins. If the detour is written in your code — `if blocked: use("Houston")` —
you have built a workflow with a branch. It will work for exactly the cases you
foresaw, and break on the first one you did not.

Checking yourself is simple: **look for the name of the detour route in your own
code.** If it is there, no replanning happened.

## Why the plan is replaced, not amended

The old plan is impossible as a whole, not in part: beyond the closed leg there
may have been stops now unreachable. The new plan takes its place, and the
history keeps both — later they show what changed and why.
