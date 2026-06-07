"""Tests for Assignment 3 — Complexity Analysis (Big O)."""

from solution import classify, count_basic_operations


def test_classify_known():
    assert classify("single pass over n items") == "O(n)"
    assert classify("nested loop over n items") == "O(n^2)"
    assert classify("one constant-time operation") == "O(1)"
    assert classify("repeatedly halving n") == "O(log n)"


def test_classify_unknown():
    assert classify("something else") == "unknown"


def test_count_basic_operations():
    assert count_basic_operations(0) == 0
    assert count_basic_operations(3) == 9
    assert count_basic_operations(10) == 100
