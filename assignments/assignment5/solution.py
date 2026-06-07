"""Assignment 5 — Stack / Queue Application.

This is the ONLY file you edit. Implement both classes, run the tests, then set
isCompleted = True at the bottom.
"""

# Flip to True after all tests pass (unlocks the Dashboard card).
isCompleted = False


class Stack:
    """Last-In, First-Out (LIFO) collection."""

    def __init__(self) -> None:
        self._items: list = []

    def push(self, value) -> None:
        """Add value to the top of the stack."""
        # TODO: append value to self._items
        raise NotImplementedError("Implement Stack.push")

    def pop(self):
        """Remove and return the top value. Raise IndexError if empty."""
        # TODO: remove and return the last item; raise IndexError if empty
        raise NotImplementedError("Implement Stack.pop")

    def is_empty(self) -> bool:
        """Return True when the stack has no items."""
        # TODO
        raise NotImplementedError("Implement Stack.is_empty")


class Queue:
    """First-In, First-Out (FIFO) collection."""

    def __init__(self) -> None:
        self._items: list = []

    def enqueue(self, value) -> None:
        """Add value to the back of the queue."""
        # TODO
        raise NotImplementedError("Implement Queue.enqueue")

    def dequeue(self):
        """Remove and return the front value. Raise IndexError if empty."""
        # TODO: remove and return the FIRST item; raise IndexError if empty
        raise NotImplementedError("Implement Queue.dequeue")

    def is_empty(self) -> bool:
        """Return True when the queue has no items."""
        # TODO
        raise NotImplementedError("Implement Queue.is_empty")
