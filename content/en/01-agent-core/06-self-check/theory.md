# Theory · Successful steps and a wrong result

On the previous level the failure came from outside: a tool said "road closed",
and the task was to notice that signal. The signal existed — it had to be read.

Here there is no signal.

All four hops were requested correctly. All four answers are correct. Not one
exception, not one error, not a line in the log. And the route is still no good:
the customer asked for forty-eight hours, and it comes out at sixty-one.

## An error in the composition

The parts are right, the whole is not. That happens whenever a result is
**assembled** rather than taken ready-made: totals, schedules, plans, estimates.

Error handling cannot catch this. Error handling catches what went wrong inside a
step. Here every step went perfectly; what did not add up is what happened
between them.

**Until somebody compares the result against the terms, nobody knows it does not
fit.** The agent included.

## Review as a separate step

There is one cure: before handing the result over, show it for checking together
with the original task.

Note the difference from an ordinary call. In the loop the model answers the
question "what do I do next". In a review it answers a different one: **"here are
the terms, here is the result, does it all add up".** The same interlocutor, a
different role.

## Why the comparison is not written in code

The temptation is strong: the deadline is known, the total is known, one line of
`if`. And for this task it would work.

But a customer usually has more than one condition: deadline, weight, paperwork,
temperature range, loading window. Every new requirement is another `if`, and six
months later nobody can read or change that tree of checks.

A model review scales differently: the conditions stay as text in the task, and
the reviewer works them out itself. **What goes into the code is not the list of
requirements but the fact that a check is mandatory.**
