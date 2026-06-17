"""Tests for Exam 1 — Test 1 Practice (Basics & OOP)."""

from solution import count_long_words, count_up_to, Employee, Manager, hire


def test_count_long_words():
    assert count_long_words([]) == 0
    assert count_long_words(["hi", "hello", "yo", "world"]) == 2  # default 4
    assert count_long_words(["a", "bb", "ccc"], 2) == 2
    assert count_long_words(["apple", "pie"], 5) == 1


def test_count_up_to():
    assert count_up_to(0) == []
    assert count_up_to(1) == [1]
    assert count_up_to(5) == [1, 2, 3, 4, 5]
    assert count_up_to(-3) == []


def test_employee_inheritance_and_override():
    assert Employee("Sam").role() == "employee"
    assert Manager("Pat").role() == "manager"
    assert Employee("Sam").describe() == "Sam: employee"
    # describe() is inherited, but uses the overridden role():
    assert Manager("Pat").describe() == "Pat: manager"
    assert isinstance(Manager("Pat"), Employee)


def test_hire_creates_correct_type():
    assert isinstance(hire("Sam"), Employee)
    assert not isinstance(hire("Sam"), Manager)
    assert isinstance(hire("Pat", True), Manager)
    assert hire("Pat", manager=True).describe() == "Pat: manager"
