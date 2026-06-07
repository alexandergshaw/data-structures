"""Tests for Assignment 7 — Binary Search Tree."""

from solution import BST


def build(values):
    tree = BST()
    for v in values:
        tree.insert(v)
    return tree


def test_in_order_is_sorted():
    tree = build([8, 3, 10, 1, 6, 14, 4, 7, 13])
    assert tree.in_order() == [1, 3, 4, 6, 7, 8, 10, 13, 14]


def test_contains():
    tree = build([5, 2, 8])
    assert tree.contains(2)
    assert tree.contains(8)
    assert not tree.contains(99)


def test_duplicates_ignored():
    tree = build([5, 5, 5])
    assert tree.in_order() == [5]
