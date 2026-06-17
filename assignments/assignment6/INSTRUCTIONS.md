# Assignment 6 — Recursive Algorithms

A **recursive** function solves a problem by calling **itself** on a smaller
version of the same problem. Every recursion needs two parts: a **base case**
(when to stop) and a **recursive case** (how to shrink the problem).

> 🧭 **No terminal.** Edit in **Codespaces**, run the **Testing** panel (🧪),
> commit/push, then open + merge a PR on GitHub.com.

## What you will build

- `factorial(n)` — `n!` by recursion.
- `repeat_string(text, n)` — build `text` repeated `n` times by recursion.

## Key ideas

- **Base case:** the smallest input you can answer immediately without recursing
  (e.g. `factorial(0) == 1`). Without it, recursion never stops!
- **Recursive case:** express the answer using the function called on a *smaller*
  input (e.g. `n * factorial(n - 1)`).
- Trust that the smaller call returns the right answer — this is the "leap of
  faith" that makes recursion click.

## Worked example (concept only — not the answer)

Counting down to zero:

```text
countdown(0) -> the base case: stop.
countdown(n) -> do something with n, then call countdown(n - 1).

So countdown(3) leads to: 3, then 2, then 1, then stop at 0.
```

`factorial` follows the same shape: stop at `0` returning `1`; otherwise return
`n` times the factorial of `n - 1`. `repeat_string` is the same idea on text:
stop at `0` returning `""`, otherwise glue one copy on to a slightly shorter
repeat. You write the Python.

## When you are done

All green ✓ → commit, push, PR, merge → Dashboard card
unlocks with a nested-recursion visualization. 🎉
