"""Tests for Review 1 — Basics & OOP."""

from solution import is_even, reverse_words, Counter


def test_is_even():
    assert is_even(0)
    assert is_even(4)
    assert not is_even(7)


def test_reverse_words():
    assert reverse_words("the quick fox") == "fox quick the"
    assert reverse_words("hello") == "hello"


def test_counter():
    c = Counter()
    assert c.value() == 0
    c.increment()
    c.increment()
    assert c.value() == 2
