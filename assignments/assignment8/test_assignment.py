"""Tests for Assignment 8 — Sorting Efficiency."""

from solution import bubble_sort, insertion_sort


CASES = [
    ([], []),
    ([1], [1]),
    ([3, 1, 2], [1, 2, 3]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([2, 2, 1, 3, 1], [1, 1, 2, 2, 3]),
]


def test_bubble_sort():
    for given, expected in CASES:
        assert bubble_sort(given) == expected


def test_insertion_sort():
    for given, expected in CASES:
        assert insertion_sort(given) == expected


def test_does_not_mutate_input():
    original = [3, 1, 2]
    bubble_sort(original)
    insertion_sort(original)
    assert original == [3, 1, 2]
