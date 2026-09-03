# Method · How to read an agent loop

A four-step procedure. It works on any agent code, yours or somebody else's.

**Step 1. Find the loop.** Look for a `while` or a `for` around the model call.
Everything inside it is one turn of the conversation.

**Step 2. Find the exit condition.** Usually `if not response.tool_calls`. No
exit condition means the code spins forever.

**Step 3. Find the limiter.** An iteration counter with a ceiling. Without one,
any mistake turns into an endless loop quietly burning money.

**Step 4. Trace one result all the way through.** Take a single tool call and
follow it with your eyes: the model asked → your code ran it → the result landed
in `messages` → the model saw it on the next iteration. **A break in that chain
is the most common failure there is.**

---

Test yourself on this level's code. Open `agent.py` and answer:

1. Which line does the loop start on?
2. Where does it end normally, and where does it end by running out of tries?
3. What goes into `messages` during one iteration, and in what order?
4. Where does the tool result get back to the model?

On the fourth question you will get stuck. That is the task.
