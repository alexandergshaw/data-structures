"""Tests for Exam 2 — Test 2 Practice."""

from solution import linear_search, reverse_with_stack, queue_after_operations


def test_linear_search():
    assert linear_search([10, 20, 30], 20) == 1
    assert linear_search([10, 20, 30], 99) == -1
    assert linear_search([], 1) == -1


def test_reverse_with_stack():
    assert reverse_with_stack([1, 2, 3]) == [3, 2, 1]
    assert reverse_with_stack([]) == []


def test_queue_after_operations():
    ops = [("enqueue", 1), ("enqueue", 2), ("dequeue",), ("enqueue", 3)]
    assert queue_after_operations(ops) == [2, 3]
    assert queue_after_operations([("dequeue",)]) == []
