"""Assignment 4 — Linked List Implementation.

This is the ONLY file you edit. Build the singly linked list, then run the tests.

A linked list is a chain of little boxes called *nodes*. Each node holds a value
and a pointer to the next node; the final node points at nothing (``None``).
Unlike a Python list there is no index — to reach an item you start at the
``head`` and follow the ``.next`` pointers one hop at a time.
"""


class Node:
    """A single link in the chain: holds a value and points to the next node."""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """A singly linked list. ``head`` is the first node (or None when empty)."""

    def __init__(self) -> None:
        self.head = None

    def append(self, value) -> None:
        """Add a new node holding ``value`` to the END of the list.

        Hint: the very first item is a special case — an empty list has no last
        node to attach to, so it becomes the head. Otherwise you have to reach
        the current last node first, and the last node is the one whose ``next``
        points at nothing.
        """
        raise NotImplementedError("Implement LinkedList.append")

    def to_list(self) -> list:
        """Return the stored values as an ordinary Python list, head first.

        Example: after ``append(1)`` then ``append(2)`` this returns ``[1, 2]``.

        Hint: begin at the head and keep following ``next`` until you fall off
        the end, collecting each value along the way.
        """
        raise NotImplementedError("Implement LinkedList.to_list")

    def __len__(self) -> int:
        """Return how many nodes are in the list (so ``len(my_list)`` works).

        Hint: nothing stores the size for you — you have to visit the nodes one
        by one and tally them. An empty list has length 0.
        """
        raise NotImplementedError("Implement LinkedList.__len__")
