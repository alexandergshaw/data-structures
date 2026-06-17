# Assignment 8 — Sorting Efficiency

Sorting is everywhere. In this assignment you implement two classic sorts **by
hand** (no built-in `sorted()`), then think about how efficient they are.

> 🧭 **No terminal.** Edit in **Codespaces**, run the **Testing** panel (🧪),
> commit/push, then open + merge a PR on GitHub.com.

## What you will build

- `bubble_sort(values)` — repeatedly swap neighboring out-of-order items.
- `selection_sort(values)` — repeatedly pick the smallest remaining item.
- `worst_case_big_o()` — **compare** the two: return the worst-case Big O they
  both share.

Both return a **new** list (the caller's list must not change) and sort in
**ascending** order.

## Key ideas

- Both of these sorts are **O(n²)** in the worst case — fine for learning, slow
  for huge inputs.
- To avoid changing the caller's list, **make a copy first** (e.g. `values[:]`)
  and sort the copy.
- A **swap** exchanges two elements; in Python you can swap with
  `a[i], a[j] = a[j], a[i]`.

## Worked example (concept only — not the answer)

One **pass** of bubble sort on `[3, 1, 2]`:

```text
compare 3 and 1 -> out of order -> swap -> [1, 3, 2]
compare 3 and 2 -> out of order -> swap -> [1, 2, 3]
```

After enough passes, no swaps are needed and the list is sorted. Selection sort
instead scans the unsorted part to find the **smallest** remaining item and
swaps it into the next spot. We described the *patterns*; you write the loops and
swaps.

## When you are done

Green checks ✓ → commit, push, PR, merge → Dashboard card
unlocks with an animated bar chart. 🎉
