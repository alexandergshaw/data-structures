"""Tests for Assignment 1 — Basic Python."""

from solution import sum_to_n, count_vowels, fizzbuzz


def test_sum_to_n():
    assert sum_to_n(1) == 1
    assert sum_to_n(5) == 15
    assert sum_to_n(100) == 5050


def test_count_vowels():
    assert count_vowels("") == 0
    assert count_vowels("Apple") == 2
    assert count_vowels("RHYTHM") == 0
    assert count_vowels("Education") == 5


def test_fizzbuzz():
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizzbuzz(15)[-1] == "FizzBuzz"
    assert fizzbuzz(3) == ["1", "2", "Fizz"]
