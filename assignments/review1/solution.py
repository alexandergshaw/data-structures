"""Review 1 — Basics & OOP.

A mixed practice set that pulls together everything from Assignments 1 and 2:

  * ``for`` and ``while`` loops, plus ``if`` conditionals;
  * writing functions that take parameters, including one with a DEFAULT value;
  * classes, inheritance, overriding, and creating instances (objects).

Nothing here is brand new — it is the same ideas in fresh problems so they stick
before Exam 1. Implement each item, then run the tests.
"""


def count_above(numbers: list, threshold: int = 0) -> int:
    """Count how many numbers are strictly greater than ``threshold``.

    This reviews three Assignment 1 ideas at once: looping over a list, an ``if``
    comparison, and a function parameter that has a DEFAULT value. Because
    ``threshold`` defaults to ``0``, ``count_above(values)`` counts the positive
    numbers — but a caller can pass any cut-off they like.

    Examples:
        count_above([1, -2, 3, 0, 5]) == 3     # uses the default threshold of 0
        count_above([1, 5, 10], 4) == 2        # only 5 and 10 clear the bar
    """
    raise NotImplementedError("Implement count_above")


def digit_sum(n: int) -> int:
    """Add up the individual digits of a non-negative whole number.

    This reviews the Assignment 1 WHILE-loop pattern: peel off the last digit,
    add it to the total, shrink the number, and repeat until nothing is left.
    For example ``123`` gives ``1 + 2 + 3 == 6``. Assume ``n >= 0``.

    Examples:
        digit_sum(123) == 6
        digit_sum(0) == 0
    """
    raise NotImplementedError("Implement digit_sum")


class Shape:
    """A generic shape.

    On its own a Shape has no real size, so ``area()`` returns ``0``. Subclasses
    replace (OVERRIDE) ``area()`` with a formula that fits their actual shape —
    exactly like ``Dog`` and ``Cat`` replaced ``speak()`` back in Assignment 2.
    """

    def area(self) -> float:
        raise NotImplementedError("Implement Shape.area")


class Rectangle(Shape):
    """A Shape that knows its width and height.

    Saves both values on the instance in ``__init__`` and OVERRIDES ``area()`` to
    return ``width * height``.
    """

    def __init__(self, width, height):
        # TODO: store width and height on the instance
        raise NotImplementedError("Implement Rectangle.__init__")

    def area(self):
        raise NotImplementedError("Implement Rectangle.area")


class Square(Rectangle):
    """A Rectangle whose sides are equal.

    A square *is a* rectangle, so it INHERITS ``area()`` with no changes — it only
    has to set its width and height to the same side length.
    """

    def __init__(self, side):
        # TODO: set both width and height to side
        raise NotImplementedError("Implement Square.__init__")


def make_squares(sides: list) -> list:
    """Build and return a list of Square OBJECTS, one per side length.

    This reviews "making instances" from Assignment 2 (like ``make_animals``):
    loop over the inputs and create a new ``Square`` for each, keeping the same
    order.

    Example:
        make_squares([2, 3])[0].area() == 4
    """
    raise NotImplementedError("Implement make_squares")
