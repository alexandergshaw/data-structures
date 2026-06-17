# Exam 3 — Test 3 Practice (Recursion, Trees, Algorithms)

The final **practice test**, covering recursion, trees, and core algorithms from
Assignments 6-8 plus Review 3.

> 🧭 **No terminal.** Edit in **Codespaces**, run the **Testing** panel (🧪),
> commit/push, then open + merge a PR on GitHub.com.

## What is on this practice test

- `gcd(a, b)` — recursion with Euclid's algorithm.
- `count_nodes(node)` — recursion over a binary tree.
- `is_sorted(values)` — check whether a list is already in ascending order.

## Exam tips

- `gcd` has a clean base case: `gcd(a, 0) == a`.
- Tree counting: a tree's node count is `1 + left count + right count`, with
  `None` counting as `0`.
- For `is_sorted`, you only need to compare **neighbouring** items; a single
  out-of-order pair is enough to answer `False`.

## Worked example (concept only — not the answer)

Checking whether `[1, 3, 2]` is sorted:

```text
compare 1 and 3 -> 1 <= 3, fine so far
compare 3 and 2 -> 3 > 2, out of order -> the list is NOT sorted
```

You only ever look at neighbouring pairs, and the first bad pair settles it. We
traced the *idea*; you implement the comparison loop.

## When you are done

Green checks ✓ → commit, push, PR, merge → Dashboard card
unlocks. You have reached the end of the course — congratulations! 🎓🎉
