"""Tests for Exam 3 — Test 3 Practice."""

from solution import gcd, count_nodes, binary_search


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


def test_binary_search():
    data = [1, 3, 5, 7, 9, 11]
    assert binary_search(data, 7) == 3
    assert binary_search(data, 1) == 0
    assert binary_search(data, 11) == 5
    assert binary_search(data, 4) == -1
    assert binary_search([], 1) == -1
