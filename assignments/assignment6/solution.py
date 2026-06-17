"""Assignment 6 — Recursive Algorithms.

This is the ONLY file you edit. Solve each one with RECURSION (no loops), then
run the tests.

A recursive function calls itself on a SMALLER version of the same problem until
it reaches a case so simple it can answer outright — the "base case". Always
handle the base case first, or the function will keep calling itself forever.
"""


def factorial(n: int) -> int:
    """Return n! (n factorial) using recursion. Assume n >= 0.

    n! is the product of every whole number from 1 up to n, and 0! is defined as
    1. So factorial(5) is 5 × 4 × 3 × 2 × 1 == 120.

    Hint: the simplest case is n == 0. For any larger n, think about how n!
    relates to the factorial of the number just below it.
    """
    raise NotImplementedError("Implement factorial")


def repeat_string(text: str, n: int) -> str:
    """Return ``text`` joined to itself ``n`` times, built with recursion.

    repeat_string("ab", 3) == "ababab"; repeat_string("x", 0) == "". Assume
    n >= 0.

    Hint: repeating something 0 times gives the empty string — that's your base
    case. Otherwise it's one copy of ``text`` followed by the result of repeating
    it one fewer time (a smaller version of the same job).
    """
    raise NotImplementedError("Implement repeat_string")
