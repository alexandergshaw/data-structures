"""Tests for Assignment 7 — Binary Search Tree."""

from solution import BST


def build(values):
    tree = BST()
    for v in values:
        tree.insert(v)
    return tree


def test_contains():
    tree = build([8, 3, 10, 1, 6, 14])
    assert tree.contains(6)
    assert tree.contains(14)
    assert not tree.contains(99)


def test_find_min():
    tree = build([8, 3, 10, 1, 6, 14])
    assert tree.find_min() == 1
    assert BST().find_min() is None


def test_insert_updates_min():
    tree = build([5, 2, 8])
    assert tree.find_min() == 2
    tree.insert(1)
    assert tree.find_min() == 1
