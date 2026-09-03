# Theory · Plan before acting

In Foundations the agent was reactive: question — call — answer. One task, one
tool, done. Real tasks are not built that way.

"How long does freight take from the border to Newark" is four legs of a route,
each of which has to be checked, and only then added up. A reactive agent checks
the first one and answers. Formally it answered. Practically it lied.

## Why this is more dangerous than it looks

An incomplete answer **does not look like an error**. The agent did not crash,
did not loop, did not say "I don't know". It produced a number, and the number is
even correct — just not the one that was asked for.

Failures like that are found by customers, not developers.

## What a plan gives you

**A plan is a list of steps obtained before the first action and written down
separately.** It gives you three things a reactive agent does not have.

**Completeness.** While unfinished items remain in the plan, the work is not
done. The agent no longer has to guess whether it did everything: it checks
against the list.

**Observability.** The plan sits in the history separately from the execution, so
the log shows both what the agent intended to do and what it actually did. The
gap between the two is the most useful line in agent debugging.

**A point to intervene.** A plan can be shown to a human before the agent starts
spending money and changing state. We come back to this on the level about the
human in the loop.

## What a plan does not give you

It does not make the agent smarter and does not guarantee the steps are right. A
plan made wrongly will be executed wrongly — the difference is that now you can
see it in the log instead of guessing it from the result.
