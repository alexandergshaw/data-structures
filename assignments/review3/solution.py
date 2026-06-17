"""Review 3 — Recursion, Trees, Sorting.

Mixed practice pulling together Assignments 6-8: recursion, binary trees, and
sorting by hand. Implement each item, then run the tests.
"""


def power(base: int, exp: int) -> int:
    """Return ``base`` raised to ``exp`` (base ** exp) using recursion.

    Assume ``exp >= 0``. For example power(2, 3) == 8.

    Hint: anything to the power 0 is 1 — that's your base case. For a larger
    exponent, think about how ``base ** exp`` relates to ``base`` raised to one
    less than ``exp``.
    """
    raise NotImplementedError("Implement power")


def tree_height(node) -> int:
    """Return the height of a binary tree: the number of steps on the LONGEST
    path from the top down to a leaf.

    A node is either ``None`` or an object with ``.left`` and ``.right``. By
    convention an empty tree (``None``) has height ``-1``, and a lone node with no
    children has height ``0``.

    Hint: a tree's height is one more than the taller of its two subtrees. The
    ``None`` case is what stops the recursion.
    """
    raise NotImplementedError("Implement tree_height")


def selection_sort(values: list) -> list:
    """Return a new ascending-sorted copy of ``values`` using selection sort.

    Selection sort builds the answer front-to-back: find the smallest item that
    is still unsorted, put it in the next position, and repeat with the rest.
    Do not use the built-in ``sorted()`` / ``list.sort()``.

    Hint: for each position, scan the unsorted remainder to locate the smallest
    item, then move it into place. Work on a copy so the original is untouched.
    """
    raise NotImplementedError("Implement selection_sort")
