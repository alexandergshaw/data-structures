"""Tests for Assignment 4 — Linked List."""

from solution import LinkedList


def test_empty_list():
    ll = LinkedList()
    assert ll.to_list() == []
    assert len(ll) == 0


def test_append_and_to_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.to_list() == [1, 2, 3]


def test_len():
    ll = LinkedList()
    for v in ["a", "b"]:
        ll.append(v)
    assert len(ll) == 2
