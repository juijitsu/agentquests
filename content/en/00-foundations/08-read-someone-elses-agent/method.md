# Method · Taking apart someone else's agent

Four steps. The same order works for any unfamiliar agent code.

**Step 1. Run it without reading.** Get the list of failures. Five lines of
output say more than fifteen minutes of reading.

**Step 2. Group the failures.** One cause usually breaks several requests. If
four out of five failed, that is more likely one defect in a shared place than
four different ones.

**Step 3. Go from symptom to location.** Use the symptom table from the theory.
Each one points at a specific area: the loop, parsing the answer, descriptions,
error handling.

**Step 4. Fix one at a time and rerun.** Do not change three places at once —
otherwise you will not know which one helped and which one broke something else.

---

Start with the defect that breaks the most requests: it is usually the most
general one, and after it the picture clears up.
