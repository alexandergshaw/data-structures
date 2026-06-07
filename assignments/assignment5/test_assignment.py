"""Tests for Assignment 5 — Stack / Queue."""

import pytest

from solution import Stack, Queue


def test_stack_lifo():
    s = Stack()
    assert s.is_empty()
    s.push(1)
    s.push(2)
    assert not s.is_empty()
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()


def test_stack_pop_empty_raises():
    with pytest.raises(IndexError):
        Stack().pop()


def test_queue_fifo():
    q = Queue()
    assert q.is_empty()
    q.enqueue("a")
    q.enqueue("b")
    assert q.dequeue() == "a"
    assert q.dequeue() == "b"
    assert q.is_empty()


def test_queue_dequeue_empty_raises():
    with pytest.raises(IndexError):
        Queue().dequeue()
