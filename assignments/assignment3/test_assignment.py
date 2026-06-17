"""Tests for Assignment 3 — Complexity Analysis (Big O)."""

from solution import running_totals, all_pairs, halving_sequence


def test_running_totals():
    assert running_totals([]) == []
    assert running_totals([5]) == [5]
    assert running_totals([1, 2, 3]) == [1, 3, 6]
    assert running_totals([2, 2, 2, 2]) == [2, 4, 6, 8]


def test_all_pairs():
    assert all_pairs([]) == []
    assert all_pairs([1]) == [(1, 1)]
    assert all_pairs([1, 2]) == [(1, 1), (1, 2), (2, 1), (2, 2)]
    # n items must produce n * n pairs — the O(n^2) shape.
    assert len(all_pairs([1, 2, 3, 4])) == 16


def test_halving_sequence():
    assert halving_sequence(1) == [1]
    assert halving_sequence(2) == [2, 1]
    assert halving_sequence(8) == [8, 4, 2, 1]
    assert halving_sequence(10) == [10, 5, 2, 1]
    # ~log2(n) + 1 values — the O(log n) shape.
    assert len(halving_sequence(16)) == 5
