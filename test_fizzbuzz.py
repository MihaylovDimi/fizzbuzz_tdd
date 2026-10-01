"""Unit tests for FizzBuzz, written before the production code (TDD)."""

from fizzbuzz import fizzbuzz


def test_returns_1_for_1():
    assert fizzbuzz(1) == "1"


def test_returns_fizz_for_3():
    assert fizzbuzz(3) == "Fizz"


def test_returns_2_for_2():
    assert fizzbuzz(2) == "2"