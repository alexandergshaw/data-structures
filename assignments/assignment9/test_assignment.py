"""Tests for Assignment 9 — Final Project Prototype (MinStack)."""

import pytest

from solution import MinStack


def test_push_pop_order():
    s = MinStack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.pop() == 1
    assert len(s) == 0


def test_get_min_tracks_minimum():
    s = MinStack()
    s.push(5)
    assert s.get_min() == 5
    s.push(3)
    assert s.get_min() == 3
    s.push(7)
    assert s.get_min() == 3
    s.pop()  # remove 7
    assert s.get_min() == 3
    s.pop()  # remove 3
    assert s.get_min() == 5


def test_empty_errors():
    s = MinStack()
    with pytest.raises(IndexError):
        s.pop()
    with pytest.raises(IndexError):
        s.get_min()
