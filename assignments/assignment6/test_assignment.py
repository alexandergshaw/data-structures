"""Tests for Assignment 6 — Recursive Algorithms."""

from solution import factorial, fib, sum_list


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_fib():
    assert [fib(i) for i in range(7)] == [0, 1, 1, 2, 3, 5, 8]


def test_sum_list():
    assert sum_list([]) == 0
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([10, -2, 5]) == 13
