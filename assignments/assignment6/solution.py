"""Assignment 6 — Recursive Algorithms.

This is the ONLY file you edit. Implement each recursive function, run the tests,
then set isCompleted = True at the bottom.
"""

# Flip to True after all tests pass (unlocks the Dashboard card).
isCompleted = False


def factorial(n: int) -> int:
    """Return n! using RECURSION (no loops).

    factorial(0) == 1, factorial(5) == 120. Assume n >= 0.
    """
    # TODO: base case (n == 0) returns 1; otherwise n * factorial(n - 1)
    raise NotImplementedError("Implement factorial")


def fib(n: int) -> int:
    """Return the n-th Fibonacci number using RECURSION.

    fib(0) == 0, fib(1) == 1, fib(n) == fib(n-1) + fib(n-2). Assume n >= 0.
    """
    # TODO: handle the two base cases, then the recursive sum
    raise NotImplementedError("Implement fib")


def sum_list(values: list) -> int:
    """Return the sum of a list using RECURSION (no loops, no built-in sum).

    sum_list([]) == 0, sum_list([1, 2, 3]) == 6
    """
    # TODO: base case empty list -> 0; otherwise first + sum_list(rest)
    raise NotImplementedError("Implement sum_list")
