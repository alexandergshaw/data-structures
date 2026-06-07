"""Tests for Exam 1 — Test 1 Practice (Basics & OOP)."""

import pytest

from solution import max_of, count_words, BankAccount


def test_max_of():
    assert max_of([3]) == 3
    assert max_of([1, 9, 4, 2]) == 9
    assert max_of([-5, -2, -9]) == -2


def test_count_words():
    assert count_words("one two three") == 3
    assert count_words("solo") == 1


def test_bank_account_deposit_withdraw():
    acc = BankAccount(100)
    acc.deposit(50)
    assert acc.get_balance() == 150
    acc.withdraw(70)
    assert acc.get_balance() == 80


def test_bank_account_overdraw_raises():
    acc = BankAccount(10)
    with pytest.raises(ValueError):
        acc.withdraw(11)
