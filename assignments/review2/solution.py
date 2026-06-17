"""Review 2 — Analysis & Linear Structures.

Mixed practice pulling together Assignments 3-5: Big O reasoning plus the stack
and queue ideas. Implement each item, then run the tests.
"""


def big_o_of_linear_search() -> str:
    """Return the Big O of scanning a list of n items once, as a short string.

    Looking at every item exactly one time is the textbook picture of "linear"
    growth.

    Hint: if doubling the input roughly doubles the work, which Big O class is
    that? Report it the usual way, like ``"O(?)"``.
    """
    raise NotImplementedError("Implement big_o_of_linear_search")


def is_balanced(text: str) -> bool:
    """Return ``True`` if the parentheses are balanced — every '(' has a matching
    ')' that comes after it.

    Examples: ``"(())"`` is balanced; ``"(()"`` is not (one '(' never closes);
    ``")("`` is not (a ')' shows up before any '(').

    Hint: think about counting how many '(' are still open as you read left to
    right. What must be true the instant you meet a ')', and what must be true
    once you reach the very end?
    """
    raise NotImplementedError("Implement is_balanced")


def first_in_first_out(items: list) -> list:
    """Return the items in the same order after running them through a queue —
    add them all, then remove them all.

    Because a queue is First-In-First-Out, what comes out matches what went in,
    so ``first_in_first_out([1, 2, 3]) == [1, 2, 3]``.

    Hint: add at one end and always remove from the OTHER end. An empty input
    simply gives back an empty list.
    """
    raise NotImplementedError("Implement first_in_first_out")
