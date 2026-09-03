# Theory · A first program, taken apart letter by letter

This level explains **everything** the task needs: what a function is, what a
parameter is, why quotes matter, how to join text, what indentation is, and how
`return` differs from `print`. None of it is assumed to be known already.

You do not have to read it start to finish: skip what you already know.

---

## Nothing to install to begin

The solve page has a terminal, and Python already runs in it — it loads
straight into the browser. Press "Solve this level", edit the code, run it.
Nothing to download.

This is not a teaching toy standing in for the real language. It is real
Python, built to run in a browser: same syntax, same errors, same messages.

Installing on your own machine is covered
[at the end of this lesson](#installing-on-your-own-machine). You will need it
later, when you want to write your own programs rather than solve the course.

---

## What a program is

A program takes something in and hands something back. Everything else is
detail.

```
input  ──▶  program  ──▶  output
```

Every task in this course has that same shape: there is a function, something
is passed to it, and it has to return something. Here the input is a person's
name and the output is a greeting for them.

---

## The function, part by part

Here is the whole construction. Every piece of it is taken apart below.

```python
def solve(name: str) -> str:
    return "Hello, " + name + "!"
```

### `def`

**What it is.** A keyword. A function declaration starts with it.

**Why.** It tells Python: what follows is not just code but a named piece of
code that can be called later.

**What breaks.** Writing `Def` or `DEF` will not work. The language
distinguishes capitals from small letters.

**What you will see:** `SyntaxError: invalid syntax`.

### `solve` — the name of the function

**What it is.** The name the function is found and called by.

**Why.** The check looks in your file for a function with exactly this name.
It will not guess that you called it `answer` or `myFunc`.

**What not to do.** Do not rename it. Throughout the course the function is
called `solve`.

**What you will see if you rename it:** "There is no function called solve in
the file."

### `(name: str)` — the parameter

This is the most important part of the lesson, and it is exactly where people
trip.

**What it is.** `name` is a **label**. Not a person's name, but the name of a
label you hang on whatever arrives from outside.

**Why.** Your function has to work with **any** name. The check will call it
five times in a row:

```
solve("Maria")   →  inside the function, name points at "Maria"
solve("John")    →  inside the function, name points at "John"
solve("Kim")     →  inside the function, name points at "Kim"
```

The same code, a different value behind the label each time.

**Which leads to the main point:** you cannot write a particular name into the
answer. It is different every time. What goes into the answer is the **label**,
and Python substitutes whatever is behind it this time round.

**What not to do.** Do not rename the parameter to a person's name:

```python
def solve(Maria: str) -> str:      # ← do not do this
    return "Hello, Maria!"
```

That is legal Python and it will not crash. But the function now returns the
same string for any input, and on the second name the check will say it
expected "Hello, John!" and got "Hello, Maria!".

**About `: str` and `-> str`.** Those are notes for a human: "text arrives
here", "text comes back out". Python does not enforce them, and the program
runs without them. Leave them as they are.

### The colon at the end of the line

**What it is.** The `:` after the closing bracket.

**Why.** It says: the header line is over, the body starts next.

**What breaks.** Forget the colon and Python cannot tell where the body begins.

**What you will see:** `SyntaxError: expected ':'`.

### Indentation

**What it is.** Four spaces at the start of the body line.

**Why.** Most languages wrap a body in curly brackets. Python marks it by
shifting right instead. Shifted means inside the function. Not shifted means
outside it.

```python
def solve(name: str) -> str:
    return "Hello, " + name + "!"
^^^^
four spaces, and they are not decoration
```

**What breaks.** No indent, and Python thinks the function body is empty.
Tab indents too, but mixing tabs and spaces in one file is not allowed and
Python complains about that separately.

**What you will see:** `IndentationError: expected an indented block`.

### `return`

**What it is.** The keyword that hands a value back to whoever called the
function.

**Why.** The check calls your function and looks at what it **returned**.

**What not to do.** Do not confuse it with `print`. That has its own section
below, because it is the second most common mistake after the parameter.

---

## Quotes: text versus label

The second place people get confused.

**What is inside quotes is letters. What is outside quotes is a label.**

```python
"Maria"     # five letters: M, a, r, i, a — and nothing more
name        # a label; behind it sits the value that arrived from outside
"name"      # four letters: n, a, m, e — not the value at all
```

Compare two lines:

```python
return "Hello, " + name + "!"     # right: the label without quotes
return "Hello, name!"             # wrong: the word "name" comes back
```

In the second line `name` ended up **inside** the quotes, so it stopped being
a label and became four letters.

**What breaks if you drop the quotes around text.** Python decides that
`Hello` is a label and goes looking for a value with that name. It does not
find one.

**What you will see:** `NameError: name 'Hello' is not defined`.

**How to remember it.** Quotes are a fence. Inside the fence letters are taken
as they are and Python does not interfere. Outside the fence, anything that
looks like a word is treated as the name of something.

---

## Joining with a plus

**What it is.** A `+` between two pieces of text joins them into one.

```python
"a" + "b"           →  "ab"
"Hello, " + "Kim"   →  "Hello, Kim"
```

**Why here.** The greeting is assembled from three parts: the text before the
name, the name, and the exclamation mark.

```python
"Hello, "  +  name  +  "!"
└─ text ─┘   └label┘  └text┘
```

**About the space.** It has to be **inside the quotes**, after the comma:

```python
"Hello, "     ← right: comma, space, closing quote
"Hello,"      ← wrong: you get "Hello,Maria!"
```

Spaces around the `+` do not affect the result, they are only for
readability. The space inside the quotes, though, is part of the text.

**What breaks if you add text to a number.** `"age: " + 30` does not work:
Python does not know what to do with letters and a number at once.

**What you will see:** `TypeError: can only concatenate str (not "int") to str`.

You will need that on the next level; there are no numbers here.

---

## `return` versus `print`

Two commands beginners mix up, and the mix-up is expensive.

```python
print("Hello, " + name + "!")     # show it on the screen
return "Hello, " + name + "!"     # hand it back to the caller
```

**`print`** writes a value to the screen and that is all. The function returns
**nothing** in the process.

**`return`** hands the value back. The check looks at exactly that.

**What you will see if you write `print`:** the first verdict line says
"returned text: no". On the screen everything will look right — which is the
galling part.

**How to remember it:** printing is for a human, returning is for a program.

---

## What happens when you get it wrong

The full list of what can go wrong on this level, and what to do.

| What you will see | What happened | What to do |
|---|---|---|
| `returned text: no` | `print` was written instead of `return` | replace `print(...)` with `return ...` |
| `names matched: 0 of 5`, strings nearly identical | one character differs | look at the arrow under the strings, it points at the exact spot |
| the same string for every name | the name is written into the text and the label is unused | return `"Hello, " + name + "!"` |
| `IndentationError` | the body is not shifted right | put four spaces at the start of the line |
| `SyntaxError` | an unclosed quote or bracket, or no colon | check that every quote and bracket is closed |
| `NameError` | text written without quotes | put the text in quotes |
| `AttributeError` mentioning `solve` | the function was renamed | give it back the name `solve` |

The verdict prints these explanations itself, in plain words. No guessing.

---

## What not to do

- **Do not rename `solve`** — the check finds the function by that name.
- **Do not rename `name`** — or rather, you may, but then the body has to use
  the new name too. Easier to leave it alone.
- **Do not write a person's name into the answer** — it is different each time.
- **Do not write `print` instead of `return`** — nothing comes back.
- **Do not mix tabs and spaces** — Python complains about that separately.
- **Do not write the code in your own language** — the keywords are English:
  `def`, `return`. Only text inside quotes and comments can be anything else.

---

## What this looks like in real code

The same thing, with a more interesting input and output:

```python
def rate_for(load: dict) -> float:
    return load["miles"] * 2.40
```

The same shape: `def`, a name, a parameter in brackets, a colon, an indent,
`return`. Only the inside differs. Everything you took apart on this level
works here as well.

---

## Installing on your own machine

Not needed to solve the course. You will want it when you start writing your
own programs.

### Windows

1. Open **python.org**, the Downloads section. The button offers the right
   version for your system by itself.
2. Run the file you downloaded. **At the bottom of the first window, tick "Add
   python.exe to PATH".** Without it the system will not know where Python
   lives and the `python` command will not work.
3. Press Install Now and wait for it to finish.
4. Open Terminal or PowerShell and type:

```
python --version
```

It should answer `Python 3.` and some digits. If it says the command is not
recognised, the tick from step 2 was not set. Run the installer again, choose
Modify and add Python to PATH.

### macOS

There is already a Python on the system, but it is old and there for the
system's own use. Install your own: either from **python.org** with an ordinary
installer, or through Homebrew if you have it: `brew install python`.

Check in Terminal:

```
python3 --version
```

On macOS the command is `python3`, not `python`. That is normal.

### Linux

Almost every distribution ships Python already. Check:

```
python3 --version
```

If it is missing: `sudo apt install python3` on Debian and Ubuntu,
`sudo dnf install python3` on Fedora, `sudo pacman -S python` on Arch.

### What to write code in

Any text editor will do. The most common choice is **VS Code**: free, and it
runs on all three systems.

Word and its relatives **will not do**: they put invisible formatting into the
file, and Python chokes on it.
