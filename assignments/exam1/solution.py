"""Exam 1 — Test 1 Practice (Basics & OOP).

Exam-style practice covering Assignments 1-2. Implement each item, run the tests,
then set isCompleted = True at the bottom.
"""

# Flip to True after all tests pass (unlocks the Dashboard card).
isCompleted = False


def max_of(values: list) -> int:
    """Return the largest value in a non-empty list WITHOUT using max()."""
    # TODO: loop and track the largest value seen so far
    raise NotImplementedError("Implement max_of")


def count_words(sentence: str) -> int:
    """Return how many words are in the sentence (words are space-separated)."""
    # TODO
    raise NotImplementedError("Implement count_words")


class BankAccount:
    """Holds a balance. deposit(amount) adds; withdraw(amount) subtracts.

    withdraw must raise ValueError if amount is greater than the balance.
    """

    def __init__(self, balance: float = 0) -> None:
        # TODO: store the starting balance
        raise NotImplementedError("Implement BankAccount.__init__")

    def deposit(self, amount: float) -> None:
        # TODO
        raise NotImplementedError("Implement BankAccount.deposit")

    def withdraw(self, amount: float) -> None:
        # TODO: raise ValueError if amount > balance, otherwise subtract
        raise NotImplementedError("Implement BankAccount.withdraw")

    def get_balance(self) -> float:
        # TODO
        raise NotImplementedError("Implement BankAccount.get_balance")
