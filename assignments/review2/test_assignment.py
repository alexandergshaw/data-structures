"""Tests for Review 2 — Analysis & Linear Structures."""

from solution import big_o_of_linear_search, is_balanced, first_in_first_out


def test_big_o_of_linear_search():
    assert big_o_of_linear_search() == "O(n)"


def test_is_balanced():
    assert is_balanced("(())")
    assert is_balanced("()()")
    assert not is_balanced("(()")
    assert not is_balanced(")(")


def test_first_in_first_out():
    assert first_in_first_out([1, 2, 3]) == [1, 2, 3]
    assert first_in_first_out([]) == []
