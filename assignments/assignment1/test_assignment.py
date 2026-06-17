"""Tests for Assignment 1 — Basic Python."""

from solution import (
    sum_to_n,
    count_vowels,
    count_positives,
    count_down,
    count_digits,
    make_greeting,
)


def test_sum_to_n():
    assert sum_to_n(1) == 1
    assert sum_to_n(5) == 15
    assert sum_to_n(100) == 5050


def test_count_vowels():
    assert count_vowels("") == 0
    assert count_vowels("Apple") == 2
    assert count_vowels("RHYTHM") == 0
    assert count_vowels("Education") == 5


def test_count_positives():
    assert count_positives([]) == 0
    assert count_positives([1, 2, 3]) == 3
    assert count_positives([-1, 0, 2, -5, 4]) == 2
    assert count_positives([-3, -2, -1]) == 0


def test_count_down():
    assert count_down(3) == [3, 2, 1]
    assert count_down(1) == [1]
    assert count_down(0) == []
    assert count_down(-2) == []


def test_count_digits():
    assert count_digits(0) == 1
    assert count_digits(7) == 1
    assert count_digits(100) == 3
    assert count_digits(12345) == 5


def test_make_greeting():
    assert make_greeting("Ada") == "Hello, Ada!"
    assert make_greeting("Ada", "Hi") == "Hi, Ada!"
    assert make_greeting("Grace", greeting="Hey") == "Hey, Grace!"
