"""Assignment 1 — Basic Python (Variables & Loops).

This is the ONLY file you edit. Implement each function, run the tests from the
Codespaces Testing panel.
"""


def sum_to_n(n: int) -> int:
    """Return the sum of all integers from 1 up to and including n.

    Example: sum_to_n(5) == 1 + 2 + 3 + 4 + 5 == 15
    Use a loop. Assume n >= 1.
    """
    raise NotImplementedError("Implement sum_to_n")


def count_vowels(text: str) -> int:
    """Return how many vowels (a, e, i, o, u) are in text.

    Treat uppercase and lowercase the same. Example: count_vowels("Apple") == 2
    """
    raise NotImplementedError("Implement count_vowels")


def count_positives(numbers: list) -> int:
    """Return how many numbers in the list are greater than 0.

    Example: count_positives([-1, 0, 2, -5, 4]) == 2
    Use a loop and an `if`. An empty list has 0 positives.
    """
    raise NotImplementedError("Implement count_positives")


def count_down(start: int) -> list:
    """Return a list counting down from start to 1 using a WHILE loop.

    Example: count_down(3) == [3, 2, 1]. If start <= 0 the list is empty.
    """
    raise NotImplementedError("Implement count_down")


def count_digits(n: int) -> int:
    """Return how many digits are in the non-negative integer n.

    Use a WHILE loop that strips one digit at a time (n // 10). Assume n >= 0.
    Example: count_digits(12345) == 5, count_digits(0) == 1.
    """
    raise NotImplementedError("Implement count_digits")


def make_greeting(name: str, greeting: str = "Hello") -> str:
    """Return a greeting that combines the greeting word and the name.

    `greeting` is a parameter with a DEFAULT of "Hello", so callers may leave
    it out. Examples:
        make_greeting("Ada") == "Hello, Ada!"
        make_greeting("Ada", "Hi") == "Hi, Ada!"
    """
    raise NotImplementedError("Implement make_greeting")
