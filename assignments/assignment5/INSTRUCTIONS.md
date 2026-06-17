# Assignment 5 — Stack / Queue Application

**Stacks** and **queues** are two of the most useful "linear" structures.
They differ only in *which end* you add and remove from.

> 🧭 **No terminal.** Edit in **Codespaces**, run the **Testing** panel (🧪),
> commit/push, then open + merge a PR on GitHub.com.

## What you will build

- `Stack` — **LIFO** (Last In, First Out): `push`, `pop`, `is_empty`.
- `Queue` — **FIFO** (First In, First Out): `enqueue`, `dequeue`, `is_empty`.
- `is_balanced(text)` — **apply** your `Stack` to check that parentheses match.

Both `pop` and `dequeue` must raise `IndexError` when called on an empty
collection.

## Key ideas

- A **stack** is like a stack of plates: you add and remove from the **top**.
- A **queue** is like a line at a shop: you join the **back** and leave from the
  **front**.
- A Python `list` already supports `append()` (add to end) and `pop()` (remove
  from end), which makes a great foundation.

## Worked example (concept only — not the answer)

Trace a stack:

```text
push(10)  -> [10]
push(20)  -> [10, 20]
pop()     -> returns 20, leaving [10]   (the LAST item came out first)
```

Trace a queue:

```text
enqueue(10) -> [10]
enqueue(20) -> [10, 20]
dequeue()   -> returns 10, leaving [20] (the FIRST item came out first)
```

Notice the only difference is **which end** you remove from. To raise an error on
empty, check `is_empty()` first and `raise IndexError(...)`.

Then **apply** your stack in `is_balanced`: reading left to right, push when you
see `(` and pop when you see `)`. A `)` with an empty stack — or leftovers at the
end — means the parentheses don't match. You write the code.

## When you are done

Green checks ✓ → commit, push, PR, merge → Dashboard card
unlocks with a stack visualization. 🎉
