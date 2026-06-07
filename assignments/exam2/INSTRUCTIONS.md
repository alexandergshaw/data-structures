# Exam 2 — Test 2 Practice (Analysis, Lists, Stacks, Queues)

A **practice test** for Test 2, covering complexity analysis and the linear
structures from Assignments 3-5 plus Review 2.

> 🧭 **No terminal.** Edit in **Codespaces**, run the **Testing** panel (🧪),
> commit/push, then open + merge a PR on GitHub.com.

## What is on this practice test

- `linear_search(values, target)` — the O(n) search (no `list.index`).
- `reverse_with_stack(values)` — use LIFO behavior to reverse a list.
- `queue_after_operations(ops)` — replay enqueue/dequeue operations.

## Exam tips

- Return **`-1`** (not an error) when a search target is missing.
- Reversing with a stack works because the **last item pushed is the first
  popped**.
- Read the operation format carefully: `("enqueue", value)` has two parts;
  `("dequeue",)` has one.

## Worked example (concept only — not the answer)

Reversing `[1, 2, 3]` with a stack:

```text
push 1, push 2, push 3   -> stack: [1, 2, 3]
pop -> 3, pop -> 2, pop -> 1
result collected in pop order: [3, 2, 1]
```

We showed the *mechanism*. You write the push/pop loops.

## When you are done

Green checks ✓ → `isCompleted = True` → commit, push, PR, merge → Dashboard card
unlocks. Good luck on Test 2! 🎉
