# Assignment 7 — Binary Search Tree (BST)

A **Binary Search Tree** keeps values sorted as you insert them. Every node has
up to two children: everything in the **left** subtree is **smaller**, and
everything in the **right** subtree is **larger**.

> 🧭 **No terminal.** Edit in **Codespaces**, run the **Testing** panel (🧪),
> commit/push, then open + merge a PR on GitHub.com.

## What you will build

A `BST` class with:

- `insert(value)` — place a value in the correct spot (ignore duplicates).
- `contains(value)` — return `True`/`False`.
- `find_min()` — return the smallest value (or `None` if the tree is empty).

A `TreeNode` class (value + left + right) is provided.

## Key ideas

- The **BST property**: at every node, `left < node < right`.
- To **insert** or **search**, compare your value to the current node and go
  **left** if smaller or **right** if larger — repeat until you find the spot.
- The **smallest value** lives at the far LEFT: from the root, keep following
  left children until there are none left.

## Worked example (concept only — not the answer)

Inserting `3` into this tree:

```text
        8
       / \
      4   10

3 is less than 8  -> go LEFT to 4
3 is less than 4  -> go LEFT, which is empty -> place 3 here

        8
       / \
      4   10
     /
    3
```

For `find_min()`, use that same "go left" instinct: the smallest value is as far
left as you can walk from the root. We showed the *path-finding* idea — you
implement the comparisons and the walk.

## When you are done

Green checks ✓ → commit, push, PR, merge → Dashboard card
unlocks with a tree diagram. 🎉
