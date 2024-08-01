"""
This module is for testing the calculator script and for maintaing complete code coverage
"""
import pytest
from calculator import add, subtract, multiply, divide, modulus


def test_add():
    """Test addition of two numbers."""
    assert add(1, 2) == 3


def test_subtract():
    """Test subtraction of two numbers."""
    assert subtract(5, 6) == -1


def test_multiply():
    """Test multiplication of two numbers."""
    assert multiply(9, 2) == 18


def test_divide():
    """Test division of two numbers."""
    assert divide(10, 5) == 2
    with pytest.raises(ValueError):  # Test raising EXCEPTION on dividing by zero
        divide(10, 0)


def test_modulus():
    """Test modulus of two numbers."""
    assert modulus(10, 3) == 1
