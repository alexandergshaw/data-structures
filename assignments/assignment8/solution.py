"""Assignment 8 — Sorting Efficiency.

This is the ONLY file you edit. Implement the two sorts by hand, then run the
tests.

Both functions return a NEW list and must leave the caller's list untouched, so
copy the input first. Do not use Python's built-in ``sorted()`` or
``list.sort()`` — the whole point is to build the ordering logic yourself and
feel how the work grows.
"""


def bubble_sort(values: list) -> list:
    """Return a new ascending-sorted copy of ``values`` using bubble sort.

    Bubble sort repeatedly compares neighbouring items and swaps any that are out
    of order. Each full pass "bubbles" the largest remaining value to the end, so
    after enough passes everything has settled into place.

    Hint: this naturally needs a loop inside a loop — one to make repeated passes
    and one to walk the neighbouring pairs within a pass. Remember to work on a
    copy.
    """
    raise NotImplementedError("Implement bubble_sort")


def selection_sort(values: list) -> list:
    """Return a new ascending-sorted copy of ``values`` using selection sort.

    Selection sort builds the result front-to-back: find the smallest item that
    is still unsorted, swap it into the next position, and repeat with the rest.

    Hint: for each position, scan the unsorted remainder to find the smallest
    item, then swap that item into place. Work on a copy.
    """
    raise NotImplementedError("Implement selection_sort")


def worst_case_big_o() -> str:
    """Return the worst-case Big O that bubble sort and selection sort SHARE.

    This is the "compare" part of the assignment: although the two sorts move
    items around differently, their efficiency is the same. Each makes about n
    passes and does about n work per pass, so both land in the same complexity
    class. Return it as a short string.

    Hint: a loop running inside another loop, each over n items — what growth
    rate is that?
    """
    raise NotImplementedError("Implement worst_case_big_o")
