"""Exam 1 — Test 1 Practice (Basics & OOP).

A practice test covering the same ground as Assignments 1-2 and Review 1:

  * ``for`` and ``while`` loops with ``if`` conditionals;
  * functions that take a parameter with a DEFAULT value;
  * classes, inheritance, overriding, and creating instances (objects).

Implement each item, then run the tests. Try to work without peeking at earlier
solutions.
"""


def count_long_words(words: list, min_length: int = 4) -> int:
    """Count how many words are at least ``min_length`` characters long.

    Reviews a loop, an ``if`` comparison, and a DEFAULT parameter: ``min_length``
    defaults to ``4``, so callers can leave it out for the common case.

    Examples:
        count_long_words(["hi", "hello", "yo", "world"]) == 2   # default 4
        count_long_words(["a", "bb", "ccc"], 2) == 2            # cut-off of 2
    """
    raise NotImplementedError("Implement count_long_words")


def count_up_to(n: int) -> list:
    """Return the list ``[1, 2, ..., n]`` built with a WHILE loop.

    Reviews the basic WHILE-loop pattern: start a counter at ``1`` and, as long
    as it hasn't passed ``n``, add it to the list and step the counter up by one.
    If ``n`` is less than ``1`` the list is empty.

    Examples:
        count_up_to(3) == [1, 2, 3]
        count_up_to(0) == []
    """
    raise NotImplementedError("Implement count_up_to")


class Employee:
    """A person on staff, identified by name.

    ``role()`` returns the generic ``"employee"``. ``describe()`` builds a label
    from the name and the role — and it calls ``role()`` rather than hard-coding
    the word, so subclasses that OVERRIDE ``role()`` automatically describe
    themselves correctly.
    """

    def __init__(self, name: str) -> None:
        # TODO: store name on the instance
        raise NotImplementedError("Implement Employee.__init__")

    def role(self) -> str:
        raise NotImplementedError("Implement Employee.role")

    def describe(self) -> str:
        raise NotImplementedError("Implement Employee.describe")


class Manager(Employee):
    """An Employee that OVERRIDES ``role()`` to return ``"manager"``.

    It inherits ``describe()`` unchanged, yet ``describe()`` now reports
    "manager" because it asks ``role()`` for the answer.
    """

    def role(self) -> str:
        raise NotImplementedError("Implement Manager.role")


def hire(name: str, manager: bool = False) -> Employee:
    """Create and return a new staff member.

    Reviews creating instances together with a DEFAULT parameter: by default you
    ``hire`` a plain ``Employee``, but ``hire(name, True)`` builds a ``Manager``.

    Examples:
        hire("Sam")            # -> an Employee
        hire("Pat", True)      # -> a Manager
    """
    raise NotImplementedError("Implement hire")
