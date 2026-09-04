# Theory · A number, and text that looks like one

On the previous level everything was text and the plus glued. Here numbers
appear, and the same plus starts to mean something else.

---

## A variable

**What it is.** A name with a value behind it.

```python
loaded = 1450
```

The name on the left, an equals sign in the middle, the value on the right.
After that line the word `loaded` can be written instead of the number 1450
anywhere.

**Why.** So a calculation can go in steps and every step can have a name that
says what it is. Compare:

```python
return miles + " + 60 = " + str(int(miles) + 60)   # all in one line

loaded = int(miles)                                 # the same thing, but you
total = loaded + 60                                 # can see what happens
return miles + " + 60 = " + str(total)
```

Both do the same. The second one reads.

**What not to do.** Do not mix up `=` and `==`. One equals means "put what is
on the right into the name on the left". Two equals is the question "are these
equal", and it comes up on the level about conditions.

**What you will see if you write a name that does not exist:**
`NameError: name 'loded' is not defined` — usually a typo.

---

## Two different kinds of value

```python
1450      # a number; you can do arithmetic with it
"1450"    # text made of four digits; you cannot
```

They look alike and behave differently. The difference is not in what is
written but in the quotes around it.

**How to check what you have.** Ask Python:

```python
type(1450)      # <class 'int'>   a whole number
type("1450")    # <class 'str'>   a string, that is, text
```

`int` from integer. `str` from string.

---

## A plus means two different things

This is the heart of the level.

```python
1450 + 60         # 1510      numbers add
"1450" + "60"     # "145060"  text glues
```

The same sign. Python looks not at the sign but at what stands on either side
of it.

**What breaks when the two sides differ.**

```python
"1450" + 60
```

Python cannot guess which you meant, gluing or adding. It refuses.

**What you will see:** `TypeError: can only concatenate str (not "int") to str`.

Word for word: only a string can be stuck onto a string, not an integer.

**What not to do.** Having read that message, a beginner usually puts quotes
around the number: `"1450" + "60"`. The error goes away and another one
arrives, a silent one: the result is `"145060"` instead of `1510`. The program
does not crash and the answer is wrong. That is exactly how this level's
starter is built.

---

## Carrying a value from one kind to the other

**`int(text)`** makes a number out of text.

```python
int("1450")     # 1450
int("0")        # 0
```

**`str(number)`** makes text out of a number.

```python
str(1510)       # "1510"
```

**Why both.** In the task the miles arrive as text and a number has to be added
to them, so `int` is needed. The answer is assembled with a plus, and a plus
between text and a number does not work, so the sum has to go back into text
through `str`.

**What breaks in `int`.** It takes digits and nothing else.

```python
int("1450 ")    # a space inside: error
int("thousand") # letters: error
int("14.5")     # a dot: error, that is not a whole number
```

**What you will see:** `ValueError: invalid literal for int() with base 10`.
Word for word: this will not do for int().

---

## What the right line of thought looks like

The task asks for one line, and in it the same value appears **twice and
differently**:

```
"1450 + 60 = 1510"
 ────           ────
 as text        as a number
```

On the left the miles are wanted exactly as they arrived — that is already
text, leave it alone. On the right a sum is wanted, and only numbers add.

Hence three steps: make a number out of the text, add, put the result back
into text.

---

## What happens when you get it wrong

| What you will see | What happened | What to do |
|---|---|---|
| an answer like `1450 + 60 = 145060` | text was glued instead of numbers added | `int(miles)` before adding |
| `TypeError: can only concatenate str` | text is being glued to a number | wrap the number in `str()` |
| `TypeError: unsupported operand` | a number is being added to text | bring both sides to one kind |
| `ValueError: invalid literal for int()` | the text is not only digits | remove the extra before `int()` |
| `returned text: no` | a number came back where text is wanted | wrap the answer in `str()` |

---

## What not to do

- **Do not put quotes around the 60** to make the `TypeError` go away. The
  error will go, and the answer will quietly become wrong.
- **Do not turn the whole answer into a number.** `int("1450 + 60 = 1510")`
  will not work: that is not only digits.
- **Do not change `miles`.** On the left of the answer it is wanted exactly as
  it arrived.

---

## What this looks like in real code

```python
def rate_line(miles: str, per_mile: float) -> str:
    total = int(miles) * per_mile
    return miles + " miles at " + str(per_mile) + " = " + str(total)
```

The same three: carry the input into a number, calculate, carry the result
back into text.
