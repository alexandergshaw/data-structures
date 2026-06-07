# Assignment 1 — Basic Python (Variables & Loops)

In this assignment you practice the building blocks of every program:
**variables**, **loops**, and **conditionals**. You will complete three small
functions in `solution.py`.

> 🧭 **No terminal.** Edit `solution.py` in **Codespaces**, run the tests from
> the **Testing** panel (the 🧪 flask icon), commit and push from the **Source
> Control** panel, then open and merge a Pull Request on GitHub.com. See
> `assignment0/INSTRUCTIONS.md` if you need the full button-by-button walkthrough.

## What you will build

| Function | Goal |
| --- | --- |
| `sum_to_n(n)` | Add up the numbers from 1 to n. |
| `count_vowels(text)` | Count the vowels in a word. |
| `fizzbuzz(n)` | The classic Fizz/Buzz list. |

## Key ideas

- A **variable** stores a value: `total = 0`.
- A **`for` loop** repeats an action: `for i in range(1, n + 1): ...`.
- `range(1, n + 1)` gives the numbers `1, 2, …, n` (the end is *exclusive*).
- An **`if` / `elif` / `else`** chooses between options.
- The **modulo** operator `%` gives a remainder: `9 % 3 == 0`, so "is it a
  multiple of 3?" is `number % 3 == 0`.

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
2. Set `isCompleted = True` in `solution.py`.
3. Commit, push, open a PR, and merge — your Dashboard card unlocks. 🎉
