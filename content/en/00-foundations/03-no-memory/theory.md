# Theory · The model remembers nothing

Every call to the model is completely independent of the previous one. It stores
no conversation context, does not remember what it answered a minute ago, and
does not recognise you between calls.

The only thing the model sees is the `messages` array you passed it right now.
Nothing else. No database, no cache, no history on its side.

Then why did the agent on earlier levels still "remember" the customer's
question? Because you resent it on every iteration. The list grew, the question
stayed at the front, and the model saw it again and again.

**An agent's memory is your array, and nothing besides.** Not a property of the
model but an engineering decision you make yourself.

From that comes a rule that saves hours of debugging: **the phrase "the agent
forgot" never describes a bug in the model.** It describes a bug in your code —
something never made it into the list, or was taken out of it.

## Three roles

The list holds messages of three kinds, and each one means something:

| Role | Who is speaking | Example |
|---|---|---|
| `user` | the customer, or you | "12-ton load, price it" |
| `assistant` | the model | answer text, or a request to call a tool |
| `tool` | your code | the result of a completed call |

The order in the list is the chronology of the conversation. The model reads it
top to bottom and reconstructs what is happening from that alone.

## The failure you cannot see

Memory loss is dangerous because **it does not look like a failure.** The agent
does not crash, does not spin, does not raise an error. It answers calmly — it
just answers wrongly, because part of the conversation never reached it.

On earlier levels the broken agent shouted about itself. This one is quiet.
