# Theory · What a program is and what you need to install

A program takes something in and hands something back. Everything else is
detail.

Every task in this course has the same shape: there is a function, something is
passed to it, and it has to return something. On this level the input is a name
and the output is a greeting. Later the input and output get more interesting;
the shape stays the same.

## You do not have to install anything

The solve page has a terminal, and Python already runs in it: it loads straight
into the browser. You can press Solve, edit code and run it without downloading
a thing.

This is not a teaching toy standing in for the real language. It is real
Python, built to run in a browser. Same language, same errors.

Sooner or later you will want to run a program on your own machine, so here is
the installation.

## Windows

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

## macOS

There is already a Python on the system, but it is old and there for the
system's own use, not for yours. Install your own:

1. Either from **python.org**, the same Downloads section, an ordinary
   installer.
2. Or through Homebrew if you have it: `brew install python`.

Check in Terminal:

```
python3 --version
```

On macOS the command is `python3`, not `python`. That is normal.

## Linux

Almost every distribution ships Python already. Check:

```
python3 --version
```

If it is missing, install the package: `sudo apt install python3` on Debian and
Ubuntu, `sudo dnf install python3` on Fedora, `sudo pacman -S python` on Arch.

## What to write code in

Any text editor will do. The most common choice is **VS Code**: it is free and
runs on all three systems. Take it if you are not already used to something
else.

Word and its relatives will not do: they put invisible formatting into the
file, and Python chokes on it.

## return, not print

Two commands beginners mix up, and the mix-up is expensive.

`print` shows a value on the screen and that is all. Whoever called your
function receives nothing.

`return` hands the value back to the caller. The check looks at exactly that,
so a solution with `print` instead of `return` does not pass, however right it
looks on screen.

The short version: **printing is for a human, returning is for a program.**
