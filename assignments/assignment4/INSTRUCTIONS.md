# Assignment 4 — Linked List Implementation

A **linked list** stores items in separate **nodes**. Each node holds a value and
a pointer to the **next** node. Unlike a Python list, items are not stored
side-by-side in memory — they are connected like a paper chain.

> 🧭 **No terminal.** Edit in **Codespaces**, run the **Testing** panel (🧪),
> commit/push, then open + merge a PR on GitHub.com.

## What you will build

A `LinkedList` class with:

- `append(value)` — add a node to the end.
- `to_list()` — return all values as a normal Python list.
- `__len__()` — so `len(my_list)` works.

A `Node` class is already provided for you (value + next pointer).

## Key ideas

- The list keeps a reference to the first node, called the **head**.
- To reach the end, you **walk**: start at `head`, then keep moving to
  `current.next` until `current.next` is `None`.
- An **empty** list has `head = None`.

## Worked example (concept only — not the answer)

Picture appending `2` to a list that already contains `1`:

```text
Before:  head -> [1 | next=None]

Walk to the last node (the one whose next is None). That is the node holding 1.
Point its `next` at a brand-new node holding 2:

After:   head -> [1 | next=*] -> [2 | next=None]
```

To `to_list()`, start at `head` and collect each `value`, hopping along `next`
until you fall off the end (`None`). We described the *walk*; you write the loop.

## When you are done

All green ✓ in the **Testing** panel → `isCompleted = True` → commit, push, PR,
merge → your linked-list visualization unlocks on the Dashboard. 🎉
