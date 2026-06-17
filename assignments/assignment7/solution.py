"""Assignment 7 — Binary Search Tree (BST) Implementation.

This is the ONLY file you edit. Build the BST, then run the tests.

A binary search tree keeps values in a sorted shape. Every node has up to two
children, and for ANY node, everything in its LEFT branch is smaller and
everything in its RIGHT branch is larger. That ordering is what makes searching
fast and lets you read the values back out already sorted.
"""


class TreeNode:
    """A node in a binary search tree: a value plus left and right children."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    """A binary search tree of comparable values (no duplicates)."""

    def __init__(self) -> None:
        self.root = None

    def insert(self, value) -> None:
        """Insert ``value`` while preserving the ordering (smaller left, larger
        right). Duplicates are ignored.

        Hint: start at the root and, at each node, decide whether the value
        belongs to its left or its right. Keep moving down that side until you
        reach an empty spot — that empty spot is exactly where the new node
        hangs. (A completely empty tree is the easy case.)
        """
        raise NotImplementedError("Implement BST.insert")

    def contains(self, value) -> bool:
        """Return ``True`` if ``value`` is somewhere in the tree.

        Hint: the ordering lets you ignore half the tree at every step — compare
        with the current node and head toward the side that COULD hold the value.
        Running out of nodes means it isn't there.
        """
        raise NotImplementedError("Implement BST.contains")

    def find_min(self):
        """Return the smallest value in the tree, or ``None`` if it is empty.

        In a BST the smallest value is always found by going LEFT — the leftmost
        node has nothing smaller than it.

        Hint: start at the root and keep stepping to the left child for as long
        as there is one. An empty tree has no minimum to return.
        """
        raise NotImplementedError("Implement BST.find_min")
