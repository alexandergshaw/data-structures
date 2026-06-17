# Review 2 — Analysis & Linear Structures

This review consolidates Assignments 3-5: **Big O analysis**, **linked lists**,
and **stacks/queues**. It is practice before Exam 2.

> 🧭 **No terminal.** Edit in **Codespaces**, run the **Testing** panel (🧪),
> commit/push, then open + merge a PR on GitHub.com.

## What you will practice

- `big_o_of_linear_search()` — recall the complexity of a single scan.
- `is_balanced(text)` — a classic **stack** application (matching parentheses).
- `first_in_first_out(items)` — model **queue** ordering.

## Refresher

- Scanning `n` items once is **O(n)**.
- A **stack** is perfect for matching brackets: push each `(`, and pop when you
  see a `)`. If you ever pop with nothing there, it is unbalanced; if anything is
  left over at the end, it is also unbalanced.
- A **queue** preserves arrival order — first in, first out.

## Worked example (concept only — not the answer)

Checking `"(()"` with a stack:

```text
'(' -> push   stack: [ ( ]
'(' -> push   stack: [ ( ( ]
')' -> pop    stack: [ ( ]
end of string -> stack is NOT empty -> unbalanced -> False
```

We walked through the *idea*. You implement the push/pop logic.

## When you are done

Green checks ✓ → commit, push, PR, merge → Dashboard card
unlocks. 🎉
