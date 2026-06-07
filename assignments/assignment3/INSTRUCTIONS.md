# Assignment 3 — Complexity Analysis (Big O)

**Big O notation** describes how the work a program does grows as its input `n`
grows. It ignores constant factors and focuses on the *shape* of the growth.

> 🧭 **No terminal.** Edit in **Codespaces**, run the **Testing** panel (🧪),
> then commit/push and open + merge a PR on GitHub.com.

## What you will build

- `classify(description)` — map a plain-English description to its Big O class.
- `count_basic_operations(n)` — count how often the inner step of a nested loop
  runs.

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
times. So the print runs `n × n = n²` times — that is **O(n²)**. Your
`count_basic_operations(n)` returns exactly that number (for example, `9` when
`n = 3`). We explained the reasoning; you write the one-line Python.

## When you are done

Green checks in the **Testing** panel ✓ → set `isCompleted = True` → commit,
push, PR, merge → Dashboard card unlocks (with a Big O growth chart!). 🎉
