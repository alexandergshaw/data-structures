"""Exam 2 — Test 2 Practice (Analysis, Lists, Stacks, Queues).

A practice test covering Assignments 3-5. Implement each item, then run the
tests. Try to work without peeking at earlier solutions.
"""


def linear_search(values: list, target) -> int:
    """Return the index of ``target`` in ``values``, or ``-1`` if it isn't there.

    This is the plain O(n) search — check items one at a time. Do not use
    ``list.index()``.

    Hint: you need the POSITION, not just whether it's present, so keep track of
    where you are as you scan. Reaching the end with no match means -1.
    """
    raise NotImplementedError("Implement linear_search")


def reverse_with_stack(values: list) -> list:
    """Return a NEW list with the items in reverse order, using a STACK idea.

    Example: ``reverse_with_stack([1, 2, 3]) == [3, 2, 1]``.

    Hint: a stack hands things back in the opposite order you put them in (last
    in, first out). What do you end up with if you push everything on, then take
    it all back off?
    """
    raise NotImplementedError("Implement reverse_with_stack")


def queue_after_operations(ops: list) -> list:
    """Replay a list of queue operations and return the queue's final contents.

    Each operation is a tuple: ``("enqueue", value)`` adds to the back, and
    ``("dequeue",)`` removes from the front. A dequeue on an empty queue is simply
    ignored. Example:
    ``[("enqueue", 1), ("enqueue", 2), ("dequeue",), ("enqueue", 3)] -> [2, 3]``.

    Hint: keep a list and handle each operation in turn — look at the operation's
    name to decide what to do, and don't try to remove from an empty queue.
    """
    raise NotImplementedError("Implement queue_after_operations")


def linear_search_complexity() -> str:
    """Return the worst-case Big O time of the ``linear_search`` above.

    This is the "analysis" part of the test: think about how many items
    ``linear_search`` might have to look at when the target is missing (or is the
    very last item). Return the matching Big O class as a short string.

    Hint: in the worst case you end up checking every item exactly once.
    """
    raise NotImplementedError("Implement linear_search_complexity")
