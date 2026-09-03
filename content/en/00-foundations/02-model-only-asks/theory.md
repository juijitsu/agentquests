# Theory · The model only asks

On the previous level you fixed the loop. Now the unpleasant news about what
actually happens inside it.

**The model cannot perform a single action.** It does not reach the internet, it
does not read files, it does not send email. All it can do is return text.

When people say "the model called a tool", here is what happened: the model
returned a structure like

```python
ToolCall(name="send_notification", arguments={"shipment_id": "TX-4471"})
```

That is a request. Nothing was sent, nothing was written anywhere. The function
is run by **your code** — and only if you wrote it to do that.

From this follows the thing that catches everybody: **the model can say it did
something it never did.** Not out of malice — it simply assembles plausible text.
The sentence "notification sent" is no different from any other sentence: it is
letters, not an event.

What you check is not the agent's words but the consequences. There is a row in
the journal — then it was sent. No row — it was not sent, whatever the agent
says about it.

The second consequence is calmer: **whatever your code can do, the agent can
do.** The agent cannot look up the ferry schedule? Then you never gave it such a
tool. No wording of the prompt fixes that — there is simply nothing to call.
