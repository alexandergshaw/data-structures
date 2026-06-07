# Review 3 — Recursion, Trees, Sorting

This review consolidates Assignments 6-8: **recursion**, **trees**, and
**sorting**. It is practice before Exam 3.

> 🧭 **No terminal.** Edit in **Codespaces**, run the **Testing** panel (🧪),
> commit/push, then open + merge a PR on GitHub.com.

## What you will practice

- `power(base, exp)` — recursion with a base case.
- `tree_height(node)` — recursion over a binary tree.
- `selection_sort(values)` — another O(n²) sort.

## Refresher

- Every recursion needs a **base case**. For `power`, that is `exp == 0`
  returning `1`.
- Tree problems are naturally recursive: an answer for a node is built from the
  answers for its **left** and **right** children.
- **Selection sort** repeatedly finds the smallest remaining item and places it
  next.

## Worked example (concept only — not the answer)

Tree height by recursion:

```text
height(None)        -> -1   (there is no node)
height(leaf)        -> 0    (a node with no children)
height(node)        -> 1 + the taller of (height(left), height(right))
```

So a root with children of heights 0 and 1 has height `1 + 1 = 2`. We described
the recurrence; you implement it.

## When you are done

Green checks ✓ → `isCompleted = True` → commit, push, PR, merge → Dashboard card
unlocks. 🎉
