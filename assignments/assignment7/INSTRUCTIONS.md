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
- `in_order()` — return all values, which for a BST comes out **sorted**.

A `TreeNode` class (value + left + right) is provided.

## Key ideas

- The **BST property**: at every node, `left < node < right`.
- To **insert** or **search**, compare your value to the current node and go
  **left** if smaller or **right** if larger — repeat until you find the spot.
- **In-order traversal** visits *left subtree → node → right subtree*, which
  produces sorted output for a BST.

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

For `in_order()`, think recursively: list everything on the left, then the
current value, then everything on the right. We showed the *path-finding* idea —
you implement the comparisons and recursion.

## When you are done

Green checks ✓ → `isCompleted = True` → commit, push, PR, merge → Dashboard card
unlocks with a tree diagram. 🎉
