# Assignment 1 — Basic Python (Variables & Loops)

In this assignment you practice the building blocks of every program:
**variables**, **loops** (both `for` and `while`), **conditionals**, and
writing your own **functions**. You will complete six small functions in
`solution.py`.

> 🧭 **No terminal.** Edit `solution.py` in **Codespaces**, run the tests from
> the **Testing** panel (the 🧪 flask icon), commit and push from the **Source
> Control** panel, then open and merge a Pull Request on GitHub.com. See
> `assignment0/INSTRUCTIONS.md` if you need the full button-by-button walkthrough.

## What you will build

| Function | Goal |
| --- | --- |
| `sum_to_n(n)` | Add up the numbers from 1 to n. |
| `count_vowels(text)` | Count the vowels in a word. |
| `count_positives(numbers)` | Count how many numbers are greater than 0. |
| `count_down(start)` | Count down from start to 1 with a `while` loop. |
| `count_digits(n)` | Count the digits in a number with a `while` loop. |
| `make_greeting(name)` | Build a greeting, with a default greeting word. |

## Key ideas

- A **variable** stores a value: `total = 0`.
- A **`for` loop** repeats an action: `for i in range(1, n + 1): ...`.
- `range(1, n + 1)` gives the numbers `1, 2, …, n` (the end is *exclusive*).
- A **`while` loop** repeats as long as its condition stays True:
  `while n > 0: ...`. Change something each pass (e.g. `n -= 1`) so it stops.
- An **`if`** runs its block only when a condition is True — e.g.
  `if number > 0:` to count a positive number.
- A **comparison** like `number > 0` is itself either `True` or `False`.
- A **function** takes inputs (**parameters**) and hands back a value with
  `return`. A parameter can have a **default**, used when the caller omits it:
  `def make_greeting(name, greeting="Hello"):`.

## Worked example (concept only — not the answer)

Suppose we want the **product** (multiplication) of `1..n` instead of the sum.
The *shape* of the loop looks like this:

```text
start a running total at 1
for each number i from 1 to n:
    multiply the running total by i
return the running total
```

Your `sum_to_n` uses the same shape, but you **add** instead of multiply and you
start the running total at `0`. Notice we described the *pattern* — you write the
actual Python yourself.

## When you are done

1. Run the **Testing** panel until every test is a green check ✓.
2. Commit, push, open a PR, and merge — once CI confirms your tests pass, your
   Dashboard card unlocks. 🎉
