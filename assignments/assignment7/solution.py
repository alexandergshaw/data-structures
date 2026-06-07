"""Assignment 7 — Binary Search Tree (BST) Implementation.

This is the ONLY file you edit. Implement the BST, run the tests, then set
isCompleted = True at the bottom.
"""

# Flip to True after all tests pass (unlocks the Dashboard card).
isCompleted = False


class TreeNode:
    """A node in a binary search tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    """A binary search tree of comparable values (no duplicates)."""

    def __init__(self) -> None:
        self.root = None

    def insert(self, value) -> None:
        """Insert value, keeping the BST property:
        smaller values go LEFT, larger values go RIGHT. Ignore duplicates.
        """
        # TODO: if empty set root; otherwise walk left/right to find the spot
        raise NotImplementedError("Implement BST.insert")

    def contains(self, value) -> bool:
        """Return True if value is in the tree."""
        # TODO: walk left/right comparing value at each node
        raise NotImplementedError("Implement BST.contains")

    def in_order(self) -> list:
        """Return values via in-order traversal (left, node, right).

        For a BST this yields the values in SORTED order.
        """
        # TODO: traverse left subtree, then node, then right subtree
        raise NotImplementedError("Implement BST.in_order")
