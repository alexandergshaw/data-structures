# Assignment 9 — Final Project Prototype (Advanced Data Structures)

For the final project you will design and prototype an **advanced data
structure**. This warm-up has you build a **MinStack**: a stack that can return
its smallest element instantly (in **O(1)** time).

> 🧭 **No terminal.** Edit in **Codespaces**, run the **Testing** panel (🧪),
> commit/push, then open + merge a PR on GitHub.com.

## What you will build

A `MinStack` class with:

- `push(value)` — add to the top.
- `pop()` — remove and return the top (`IndexError` if empty).
- `get_min()` — return the current smallest value **without** removing it
  (`IndexError` if empty).

## Key ideas

- A naive `get_min()` could scan the whole stack — that is **O(n)**. The goal is
  **O(1)**.
- A classic trick: keep a **second stack** that always has the *current minimum*
  on top. When you push, also push the new minimum; when you pop, pop both.
- This trades a little extra memory for much faster `get_min()` — a real example
  of the time/space trade-offs you have studied all semester.

## Worked example (concept only — not the answer)

```text
push(5)  -> values: [5]        mins: [5]
push(3)  -> values: [5,3]      mins: [5,3]   (3 < 5, so min is now 3)
push(7)  -> values: [5,3,7]    mins: [5,3,3] (7 is not smaller, repeat 3)
get_min() -> top of mins -> 3
pop()    -> removes 7 from both -> mins: [5,3], min back-tracks correctly
```

We sketched the *strategy* (a parallel "mins" stack). You decide the details and
write the Python — that is the spirit of a prototype.

## When you are done

Green checks ✓ → `isCompleted = True` → commit, push, PR, merge → your final
Dashboard card unlocks. Congratulations on reaching the prototype stage! 🎉
