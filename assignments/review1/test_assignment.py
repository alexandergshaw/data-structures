"""Tests for Review 1 — Basics & OOP."""

from solution import count_above, digit_sum, Shape, Rectangle, Square, make_squares


def test_count_above():
    assert count_above([]) == 0
    assert count_above([1, -2, 3, 0, 5]) == 3  # default threshold of 0
    assert count_above([1, 5, 10], 4) == 2
    assert count_above([-3, -1], -2) == 1  # only -1 is greater than -2


def test_digit_sum():
    assert digit_sum(0) == 0
    assert digit_sum(9) == 9
    assert digit_sum(123) == 6
    assert digit_sum(4050) == 9


def test_shape_inheritance_and_override():
    assert Shape().area() == 0
    assert Rectangle(3, 4).area() == 12
    assert Square(5).area() == 25
    assert isinstance(Square(5), Rectangle)
    assert isinstance(Square(5), Shape)


def test_make_squares():
    squares = make_squares([2, 3])
    assert len(squares) == 2
    assert all(isinstance(s, Square) for s in squares)
    assert squares[0].area() == 4
    assert make_squares([]) == []
