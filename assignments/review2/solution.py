"""Review 2 — Analysis & Linear Structures.

Mixed practice covering Assignments 3-5 (Big O, linked lists, stacks/queues).
Implement each item, run the tests, then set isCompleted = True.
"""

# Flip to True after all tests pass (unlocks the Dashboard card).
isCompleted = False


def big_o_of_linear_search() -> str:
    """Return the Big O of scanning a list of n items once. Return "O(n)"."""
    # TODO
    raise NotImplementedError("Implement big_o_of_linear_search")


def is_balanced(text: str) -> bool:
    """Return True if every '(' has a matching ')' in the right order.

    Use a STACK idea. Examples: "(())" -> True, "(()" -> False, ")(" -> False.
    """
    # TODO: push on '(' and pop on ')'; unmatched -> False
    raise NotImplementedError("Implement is_balanced")


def first_in_first_out(items: list) -> list:
    """Simulate a queue: enqueue all items, then dequeue them all into a list.

    The returned order should equal the input order. Use list operations.
    """
    # TODO
    raise NotImplementedError("Implement first_in_first_out")
