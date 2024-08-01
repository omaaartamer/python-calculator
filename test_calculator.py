"""
This module is for testing the calculator script and for maintaing complete code coverage
"""
import pytest
from calculator import add, subtract, multiply, divide, modulus


def test_add():
    """Test addition of two numbers."""
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(1000, 2000) == 3000


def test_subtract():
    """Test subtraction of two numbers."""
    assert subtract(5, 6) == -1
    assert subtract(0, 0) == 0
    assert subtract(10, 10) == 0
    assert subtract(5, 6) == -1
    assert subtract(6, 5) == 1


def test_multiply():
    """Test multiplication of two numbers."""
    assert multiply(9, 2) == 18
    assert multiply(0, 10) == 0
    assert multiply(10, 0) == 0
    assert multiply(-1, 10) == -10
    assert multiply(5, 6) == 30


def test_divide():
    """Test division of two numbers."""
    assert divide(10, 5) == 2
    with pytest.raises(ValueError):  # Test raising EXCEPTION on dividing by zero
        divide(10, 0)


def test_modulus():
    """Test modulus of two numbers."""
    assert modulus(10, 3) == 1
    assert modulus(10, 3) == 1
    assert modulus(10, 5) == 0
    assert modulus(10, 7) == 3
