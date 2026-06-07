"""Assignment 1 — Basic Python (Variables & Loops).

This is the ONLY file you edit. Implement each function, run the tests from the
Codespaces Testing panel, then set isCompleted = True at the bottom.
"""

# Flip to True after all tests pass (unlocks the Dashboard card).
isCompleted = False


def sum_to_n(n: int) -> int:
    """Return the sum of all integers from 1 up to and including n.

    Example: sum_to_n(5) == 1 + 2 + 3 + 4 + 5 == 15
    Use a loop. Assume n >= 1.
    """
    # TODO: use a loop to add up the numbers 1..n
    raise NotImplementedError("Implement sum_to_n")


def count_vowels(text: str) -> int:
    """Return how many vowels (a, e, i, o, u) are in text.

    Treat uppercase and lowercase the same. Example: count_vowels("Apple") == 2
    """
    # TODO: loop over each character and count the vowels
    raise NotImplementedError("Implement count_vowels")


def fizzbuzz(n: int) -> list[str]:
    """Return a list for 1..n where multiples of 3 -> "Fizz", 5 -> "Buzz",
    both -> "FizzBuzz", otherwise the number as a string.

    Example: fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    """
    # TODO: build and return the list using a loop
    raise NotImplementedError("Implement fizzbuzz")
