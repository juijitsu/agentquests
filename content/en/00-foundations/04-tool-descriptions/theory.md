# Theory · A tool is sold by its description

When you give an agent a tool, the model receives exactly three things about it:

```python
{
    "name": "check_border_status",
    "description": "Shows the queue and wait time at a border crossing.",
    "parameters": {"crossing": "string"},
}
```

The name, the description and the parameter schema. **It never sees your code.**
Not the body of the function, not where the data comes from, not the comments
next to it.

So choosing a tool is choosing by description and by nothing else. Two tools with
similar descriptions will get confused by the model, the same way a person handed
two identical labels would.

## The description is code

From this comes a thought that is hard to get used to: **a tool description is
part of the program, not a comment on it.** A string in quotes defines the
system's behaviour as directly as a condition in an `if`.

An unpleasant consequence follows. The compiler will not check the description.
Tests that call the function directly pass too — they never read descriptions.
The build is green, everything looks fine, and the agent picks the wrong tool.

**Nine cases out of ten of "the agent is stupid" are a description problem**, and
they are fixed in two minutes by editing text.

## What makes a description good

Three things, and all three are about the model, not about the reader of the
code:

**The situation it applies to.** Not "what the function does" but "when to call
it". The model is choosing among several — it needs something to tell them apart.

**Allowed values.** List them right in the description. That cuts down invented
arguments more reliably than any validation.

**Words from the domain.** The user will ask "how long is the wait at the
crossing" — let those same words appear in the description. The model matches the
request against the description.
