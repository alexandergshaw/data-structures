"""Exam 3 — Test 3 Practice (Recursion, Trees, Algorithms).

A practice test covering Assignments 6-8. Implement each item, then run the
tests. Try to work without peeking at earlier solutions.
"""


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of ``a`` and ``b`` using recursion.

    The GCD is the largest whole number that divides both values evenly — for
    example gcd(12, 8) == 4.

    Hint (Euclid's idea): the GCD of two numbers is the same as the GCD of the
    smaller number and the remainder left over when you divide them. Repeat that
    and the second number shrinks toward 0 — and when it reaches 0 the answer is
    sitting in the other one.
    """
    raise NotImplementedError("Implement gcd")


def count_nodes(node) -> int:
    """Return how many nodes are in a binary tree.

    A node is either ``None`` (an empty spot) or an object with ``.left`` and
    ``.right``. So ``count_nodes(None) == 0`` and a single lone node counts as 1.

    Hint: the count of a tree is itself plus the counts of its two subtrees. The
    empty (``None``) case is what ends the recursion.
    """
    raise NotImplementedError("Implement count_nodes")


def is_sorted(values: list) -> bool:
    """Return ``True`` if ``values`` is in non-decreasing (ascending) order.

    An empty list or a single item counts as sorted. For example
    ``is_sorted([1, 2, 2, 3])`` is ``True`` and ``is_sorted([1, 3, 2])`` is
    ``False``.

    Hint: compare each item with the one right after it. If any item is bigger
    than its neighbour, the list is out of order.
    """
    raise NotImplementedError("Implement is_sorted")
