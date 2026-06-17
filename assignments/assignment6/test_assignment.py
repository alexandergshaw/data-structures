"""Tests for Assignment 6 — Recursive Algorithms."""

from solution import factorial, repeat_string


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_repeat_string():
    assert repeat_string("ab", 3) == "ababab"
    assert repeat_string("x", 1) == "x"
    assert repeat_string("hi", 0) == ""
