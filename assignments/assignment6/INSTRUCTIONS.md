# Assignment 6 — Recursive Algorithms

A **recursive** function solves a problem by calling **itself** on a smaller
version of the same problem. Every recursion needs two parts: a **base case**
(when to stop) and a **recursive case** (how to shrink the problem).

> 🧭 **No terminal.** Edit in **Codespaces**, run the **Testing** panel (🧪),
> commit/push, then open + merge a PR on GitHub.com.

## What you will build

- `factorial(n)` — `n!` by recursion.
- `fib(n)` — the n-th Fibonacci number by recursion.
- `sum_list(values)` — sum a list by recursion (no loops, no built-in `sum`).

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
`n` times the factorial of `n - 1`. `fib` has **two** base cases (`0` and `1`)
and adds the two previous calls. You write the Python.

## When you are done

All green ✓ → `isCompleted = True` → commit, push, PR, merge → Dashboard card
unlocks with a nested-recursion visualization. 🎉
