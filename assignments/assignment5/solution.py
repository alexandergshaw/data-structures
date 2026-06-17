"""Assignment 5 — Stack / Queue Application.

This is the ONLY file you edit. Implement both classes, then run the tests.

A Stack is Last-In, First-Out (LIFO) — like a stack of plates, you add to and
take from the TOP. A Queue is First-In, First-Out (FIFO) — like a line at a
checkout, the first to arrive is the first served. Both can sit on top of a plain
Python list; the real decision is WHICH end you add to and remove from.
"""


class Stack:
    """Last-In, First-Out (LIFO) collection."""

    def __init__(self) -> None:
        self._items: list = []

    def push(self, value) -> None:
        """Add ``value`` to the top of the stack.

        Hint: a Python list grows cheaply at one end — let that end be your
        "top".
        """
        raise NotImplementedError("Implement Stack.push")

    def pop(self):
        """Remove and return the top value; raise ``IndexError`` if empty.

        Hint: "last in, first out" means you hand back the value added most
        recently. Check for the empty case first so you never remove from
        nothing.
        """
        raise NotImplementedError("Implement Stack.pop")

    def is_empty(self) -> bool:
        """Return ``True`` when the stack holds no items.

        Hint: this is really just a question about how many items are stored.
        """
        raise NotImplementedError("Implement Stack.is_empty")


class Queue:
    """First-In, First-Out (FIFO) collection."""

    def __init__(self) -> None:
        self._items: list = []

    def enqueue(self, value) -> None:
        """Add ``value`` to the back of the queue.

        Hint: new arrivals join at the end of the line.
        """
        raise NotImplementedError("Implement Queue.enqueue")

    def dequeue(self):
        """Remove and return the front value; raise ``IndexError`` if empty.

        Hint: "first in, first out" means you serve whoever has waited longest —
        the item at the FRONT, not the back. Check for the empty case first.
        """
        raise NotImplementedError("Implement Queue.dequeue")

    def is_empty(self) -> bool:
        """Return ``True`` when the queue holds no items.

        Hint: like the stack, this just depends on how many items are stored.
        """
        raise NotImplementedError("Implement Queue.is_empty")


def is_balanced(text: str) -> bool:
    """APPLY a Stack to check whether the parentheses in ``text`` are balanced.

    This is the classic real use of a stack: push for each '(' and pop for each
    ')'. If a ')' shows up with nothing to pop, or anything is still left at the
    end, the parentheses are not balanced. Examples: "(())" -> True, "(()" ->
    False, ")(" -> False, "" -> True.

    Hint: use the ``Stack`` you built above — push on an opener, and on a closer
    make sure there is something to pop first. The text is balanced only if the
    stack ends up empty.
    """
    raise NotImplementedError("Implement is_balanced")
