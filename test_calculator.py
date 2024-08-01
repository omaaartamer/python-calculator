import pytest
from calculator import add, subtract, multiply, divide, modulus
def test_add():
    assert add(1,2) == 3
def test_subtract():
    assert subtract(5,6) == 1
def test_multiply():
    assert multiply(9,2) == 18
def test_multiply():
    assert multiply(9,2) == 18
def test_divide():
    assert divide(10,5) == 2
    with pytest.raises(ValueError):
        divide(10,0)
def test_modulus():
    assert modulus(10,3) == 1
        
