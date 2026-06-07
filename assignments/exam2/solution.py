"""Exam 2 — Test 2 Practice (Analysis, Lists, Stacks, Queues).

Exam-style practice covering Assignments 3-5. Implement each item, run the tests,
then set isCompleted = True.
"""

# Flip to True after all tests pass (unlocks the Dashboard card).
isCompleted = False


def linear_search(values: list, target) -> int:
    """Return the index of target in values, or -1 if not present.

    This runs in O(n) time. Do not use list.index().
    """
    # TODO: loop with an index and compare each item to target
    raise NotImplementedError("Implement linear_search")


def reverse_with_stack(values: list) -> list:
    """Return a NEW list with the items reversed, using a STACK idea.

    Example: reverse_with_stack([1, 2, 3]) == [3, 2, 1]
    """
    # TODO: push everything, then pop everything into a result list
    raise NotImplementedError("Implement reverse_with_stack")


def queue_after_operations(ops: list) -> list:
    """Process a list of operations on a queue and return the final contents.

    Each op is a tuple: ("enqueue", value) or ("dequeue",).
    A dequeue on an empty queue should be ignored.
    """
    # TODO: maintain a list; enqueue appends, dequeue removes from the front
    raise NotImplementedError("Implement queue_after_operations")
