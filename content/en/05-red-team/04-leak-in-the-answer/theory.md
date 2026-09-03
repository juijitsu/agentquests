# Theory · A deputy with broad rights

For three levels you have been looking at what goes in: which inputs come from
outside, which text gets carried out as an order, which arguments bring in a
foreign value. Here the direction changes. Now what matters is **what comes
out.**

## Why the tool does not save you

The agent's tools have access checks. They are not for show: `get_docs` really
will refuse if you reach into a folder that is not yours.

Except that it checks the **agent's** rights. And the agent is the dispatch
system. To work out a rate it has to see the whole lane: other carriers' loads,
other carriers' rates, brokers' documents. Its rights are broad, and that is
not a mistake, that is its job.

The asker's rights are narrow. They see their own.

Between those two sets there is not a single check. The tool asked "is the
agent allowed" and got "yes". Nobody was put in place to ask "is the person who
will read this allowed".

## The red team's mistake

The check goes like this: make the agent call a tool it is not entitled to. It
does not work, because it is entitled to almost everything. Into the report:
access control works.

Then attention moves to the log. The log shows refusals, and they look like
evidence: somebody reached for what was not theirs and the tool blocked it. The
refusals go into the report as findings.

It is the other way round. **A refusal is proof that the control worked.** It
means the data did not go out. A real leak has no refusal in the log at all:
every call was allowed, because the agent really is allowed all of it.

Hence the rule: **a leak is a property of the answer, not of the log.**

## Why it is hard to spot by eye

The agent does not forward a record. It retells. A foreign rate arrives not as
a table with somebody else's name at the top, but as a number inside a sentence
assembled specifically for the asker: "yours is 2.90, the load next to it is
2.55". The second number belongs to somebody else, and nothing in the sentence
says so.

That is exactly why you look not at the text of the answer but at the facts it
was assembled from, and ask each one who owns it.

## The boundaries

This is still a report, not a fix. The fix goes on the way out: before the
answer is handed over, the asker's rights get checked again, this time against
the facts. The agent has no such check, and your job is to show that its
absence costs two specific requests, not an argument.
