"""Assignment 9 — Final Project Prototype (Advanced Data Structures).

This is the ONLY file you edit. Implement the MinStack, run the tests, then set
isCompleted = True at the bottom.

A MinStack is a normal stack that can also report its smallest value in O(1)
time. It is a great warm-up for your final project.
"""

# Flip to True after all tests pass (unlocks the Dashboard card).
isCompleted = False


class MinStack:
    """A stack that also tracks the minimum value efficiently."""

    def __init__(self) -> None:
        self._items: list = []
        # Hint: a second stack that mirrors the running minimum makes get_min()
        # an O(1) operation. You may design this however you like.
        self._mins: list = []

    def push(self, value) -> None:
        """Add value to the top of the stack."""
        # TODO: push value and keep the running minimum up to date
        raise NotImplementedError("Implement MinStack.push")

    def pop(self):
        """Remove and return the top value. Raise IndexError if empty."""
        # TODO: pop value and keep the running minimum consistent
        raise NotImplementedError("Implement MinStack.pop")

    def get_min(self):
        """Return (without removing) the smallest value currently in the stack.

        Raise IndexError if the stack is empty.
        """
        # TODO: return the current minimum in O(1)
        raise NotImplementedError("Implement MinStack.get_min")

    def __len__(self) -> int:
        return len(self._items)
