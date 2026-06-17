"""Tests for Exam 3 — Test 3 Practice."""

from solution import gcd, count_nodes, is_sorted


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def test_gcd():
    assert gcd(12, 8) == 4
    assert gcd(17, 5) == 1
    assert gcd(10, 0) == 10


def test_count_nodes():
    assert count_nodes(None) == 0
    assert count_nodes(Node()) == 1
    assert count_nodes(Node(Node(), Node(Node()))) == 4


def test_is_sorted():
    assert is_sorted([]) is True
    assert is_sorted([5]) is True
    assert is_sorted([1, 2, 2, 3]) is True
    assert is_sorted([1, 3, 2]) is False
    assert is_sorted([3, 2, 1]) is False
