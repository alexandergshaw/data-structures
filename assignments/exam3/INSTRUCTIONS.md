# Exam 3 — Test 3 Practice (Recursion, Trees, Algorithms)

The final **practice test**, covering recursion, trees, and core algorithms from
Assignments 6-9 plus Review 3.

> 🧭 **No terminal.** Edit in **Codespaces**, run the **Testing** panel (🧪),
> commit/push, then open + merge a PR on GitHub.com.

## What is on this practice test

- `gcd(a, b)` — recursion with Euclid's algorithm.
- `count_nodes(node)` — recursion over a binary tree.
- `binary_search(sorted_values, target)` — the O(log n) search.

## Exam tips

- `gcd` has a clean base case: `gcd(a, 0) == a`.
- Tree counting: a tree's node count is `1 + left count + right count`, with
  `None` counting as `0`.
- **Binary search** only works on **sorted** input. Keep `low`/`high` bounds and
  jump to the middle each step, halving the range.

## Worked example (concept only — not the answer)

Binary search for `7` in `[1, 3, 5, 7, 9, 11]`:

```text
low=0, high=5, middle index=2 -> value 5; 7 > 5, search the RIGHT half
low=3, high=5, middle index=4 -> value 9; 7 < 9, search the LEFT half
low=3, high=3, middle index=3 -> value 7; found! return 3
```

Each step throws away half the remaining items — that is why it is O(log n). We
traced the *idea*; you implement the bounds and comparisons.

## When you are done

Green checks ✓ → `isCompleted = True` → commit, push, PR, merge → Dashboard card
unlocks. You have reached the end of the course — congratulations! 🎓🎉
