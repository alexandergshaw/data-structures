# Assignment 3 — Complexity Analysis (Big O)

**Big O notation** describes how the work a program does grows as its input `n`
grows. It ignores constant factors and focuses on the *shape* of the growth.

> 🧭 **No terminal.** Edit in **Codespaces**, run the **Testing** panel (🧪),
> then commit/push and open + merge a PR on GitHub.com.

## What you will build

You don't *describe* the complexity — you **build the loops** that achieve it:

- `running_totals(numbers)` — write **one loop** (`O(n)`) that returns the
  running cumulative totals.
- `all_pairs(items)` — write **two nested loops** (`O(n^2)`) that return every
  ordered `(first, second)` pair.
- `halving_sequence(n)` — write a **`while` loop** (`O(log n)`) that halves `n`
  to 1 and returns the values it visits.

Each task lines up with one row of the **Key ideas** table below. The tests
check the result your loops must produce, so a shortcut formula won't pass.

## Key ideas

| Pattern | Big O | Intuition |
| --- | --- | --- |
| One step, no loop | `O(1)` | Constant — same work no matter how big `n` is. |
| One loop over `n` | `O(n)` | Linear — double `n`, double the work. |
| Loop inside a loop | `O(n^2)` | Quadratic — work grows with the square of `n`. |
| Halving `n` each step | `O(log n)` | Logarithmic — very slow growth. |

## Worked example (concept only — not the answer)

How many times does the `print` run here?

```text
for i in range(n):
    for j in range(n):
        print(i, j)
```

The outer loop runs `n` times; for **each** of those, the inner loop runs `n`
times, so the body runs `n × n = n²` times — that is **O(n²)**. This is exactly
the shape your `all_pairs(items)` must build: collect each `(i, j)` pair instead
of printing it. We showed the *shape* of the nested loops; you write them (and
the single loop and the halving loop) yourself.

## When you are done

Green checks in the **Testing** panel ✓ → commit,
push, PR, merge → Dashboard card unlocks (with a Big O growth chart!). 🎉
