"""Tests for Assignment 0 — Environment Setup.

These tests import from `solution.py` (the file you edit). Run them from the
Codespaces **Testing** panel. Every test should show a green check once you have
completed the assignment.
"""

from solution import hello_course


def test_hello_course_returns_exact_greeting():
    assert hello_course() == "Hello, Algorithms!"


def test_hello_course_returns_a_string():
    assert isinstance(hello_course(), str)
