"""Assignment 3 — Complexity Analysis (Big O).

This is the ONLY file you edit. Implement the functions, run the tests, then set
isCompleted = True at the bottom.
"""

# Flip to True after all tests pass (unlocks the Dashboard card).
isCompleted = False


def classify(operations: str) -> str:
    """Return the Big O class for a short description string.

    Map these inputs (exactly) to their complexity:
      "single pass over n items"        -> "O(n)"
      "nested loop over n items"        -> "O(n^2)"
      "one constant-time operation"     -> "O(1)"
      "repeatedly halving n"            -> "O(log n)"
    Return "unknown" for anything else.
    """
    # TODO: use a dict or if/elif to map the description to its Big O class
    raise NotImplementedError("Implement classify")


def count_basic_operations(n: int) -> int:
    """Return how many times the innermost step runs in a nested loop.

    For two nested loops that each run n times, the inner body runs n * n times.
    Example: count_basic_operations(3) == 9
    """
    # TODO: return the count for two nested loops over n
    raise NotImplementedError("Implement count_basic_operations")
