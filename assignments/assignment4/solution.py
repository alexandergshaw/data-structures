"""Assignment 4 — Linked List Implementation.

This is the ONLY file you edit. Implement the LinkedList, run the tests, then set
isCompleted = True at the bottom.
"""

# Flip to True after all tests pass (unlocks the Dashboard card).
isCompleted = False


class Node:
    """A single link in the chain: holds a value and points to the next node."""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """A singly linked list."""

    def __init__(self) -> None:
        self.head = None

    def append(self, value) -> None:
        """Add a new node holding `value` to the END of the list."""
        # TODO: if the list is empty, set head; otherwise walk to the last node
        raise NotImplementedError("Implement LinkedList.append")

    def to_list(self) -> list:
        """Return the values as a normal Python list, head first.

        Example: after append(1), append(2) -> [1, 2]
        """
        # TODO: walk from head to the end, collecting values
        raise NotImplementedError("Implement LinkedList.to_list")

    def __len__(self) -> int:
        """Return how many nodes are in the list."""
        # TODO: count the nodes by walking from head
        raise NotImplementedError("Implement LinkedList.__len__")
