"""Exam 3 — Test 3 Practice (Recursion, Trees, Algorithms).

Exam-style practice covering Assignments 6-9. Implement each item, run the tests,
then set isCompleted = True.
"""

# Flip to True after all tests pass (unlocks the Dashboard card).
isCompleted = False


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b using RECURSION.

    Use Euclid's rule: gcd(a, 0) == a; otherwise gcd(b, a % b).
    """
    # TODO
    raise NotImplementedError("Implement gcd")


def count_nodes(node) -> int:
    """Return the number of nodes in a binary tree.

    A node is None (0) or an object with .left and .right.
    """
    # TODO: 0 for None; otherwise 1 + count_nodes(left) + count_nodes(right)
    raise NotImplementedError("Implement count_nodes")


def binary_search(sorted_values: list, target) -> int:
    """Return the index of target in an ASCENDING sorted list, or -1.

    Must run in O(log n) by repeatedly halving the search range.
    """
    # TODO: track low/high bounds and compare against the middle element
    raise NotImplementedError("Implement binary_search")
