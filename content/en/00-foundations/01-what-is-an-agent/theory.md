# Theory · What is actually going on

The word "agent" sounds like something complicated is hidden inside. What is
hidden inside is a `while` loop, and that is not a simplification — that is
literally all of it.

Every agent has exactly three parts.

**The model** is the thing that picks the next step. It executes nothing itself
and remembers nothing between calls.

**Tools** are ordinary functions in your code. Look up a shipment, price a load,
send an email. The model does not run them; it only asks for them to be run.

**The loop** is your code, tying the first to the second. Ask the model, get a
request to call a tool, call it, put the result back, ask again. On and on until
the model says: that is it, here is the answer.

Here it is in full:

```python
messages = [{"role": "user", "content": "Where is shipment TX-4471?"}]

while True:
    response = model.call(messages, tools=TOOLS)
    messages.append({"role": "assistant", ...})

    if not response.tool_calls:
        return response.text                 # done

    for call in response.tool_calls:
        result = run_tool(call.name, call.arguments)
        messages.append({"role": "tool", "content": result})
```

Twelve lines. Whatever you are shown later — LangGraph, the OpenAI Agents SDK,
somebody's thousand-line framework — this is what is inside.

Look closely at the `messages` list. It grows on every iteration, and it holds
everything the agent knows about what is happening: the user's question, the
request to call a tool, the result of that call. On every step the model sees
this list in full and nothing besides it.

From that follows the one fact that explains half of the bugs ahead of you:
**if something did not make it into `messages`, for the model it does not
exist.**
