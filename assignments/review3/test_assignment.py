"""Tests for Review 3 — Recursion, Trees, Sorting."""

from solution import power, tree_height, selection_sort


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def test_power():
    assert power(2, 0) == 1
    assert power(2, 3) == 8
    assert power(5, 2) == 25


def test_tree_height():
    assert tree_height(None) == -1
    assert tree_height(Node()) == 0
    assert tree_height(Node(Node(), Node(Node()))) == 2


def test_selection_sort():
    assert selection_sort([]) == []
    assert selection_sort([3, 1, 2]) == [1, 2, 3]
    assert selection_sort([5, 4, 4, 1]) == [1, 4, 4, 5]
