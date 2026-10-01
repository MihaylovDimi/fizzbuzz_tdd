"""FizzBuzz production code, written only to make failing tests pass."""
"""Unit tests for FizzBuzz, written before the production code (TDD)."""

from fizzbuzz import fizzbuzz


def test_returns_1_for_1():
    assert fizzbuzz(1) == "1"