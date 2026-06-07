"""Review 3 — Recursion, Trees, Sorting.

Mixed practice covering Assignments 6-8. Implement each item, run the tests, then
set isCompleted = True.
"""

# Flip to True after all tests pass (unlocks the Dashboard card).
isCompleted = False


def power(base: int, exp: int) -> int:
    """Return base ** exp using RECURSION. Assume exp >= 0. power(2, 3) == 8."""
    # TODO: base case exp == 0 -> 1; otherwise base * power(base, exp - 1)
    raise NotImplementedError("Implement power")


def tree_height(node) -> int:
    """Return the height of a binary tree.

    A node is either None (height -1) or an object with .left and .right.
    A single node (no children) has height 0.
    """
    # TODO: recursive case -> 1 + max(height(left), height(right))
    raise NotImplementedError("Implement tree_height")


def selection_sort(values: list) -> list:
    """Return a NEW ascending-sorted list using selection sort.

    Do not use built-in sorted()/list.sort().
    """
    # TODO: repeatedly select the smallest remaining item
    raise NotImplementedError("Implement selection_sort")
