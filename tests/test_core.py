"""Integration tests for the Petal package."""
import pytest

from petal.core import add, greet


def test_greet_returns_greeting():
    assert greet("World") == "Hello, World!"


def test_greet_with_different_names():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"


def test_add_two_positive_numbers():
    assert add(2, 3) == 5


def test_add_with_zero():
    assert add(0, 10) == 10


def test_add_negative_numbers():
    assert add(-1, -2) == -3
