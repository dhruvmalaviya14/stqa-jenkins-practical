import pytest
from calculator import add, subtract, multiply, divide

def test_addition():
    assert add(10, 5) == 15


# def test_intentional_failure():
#     assert add(2,2) == 5

def test_subtraction():
    assert subtract(10, 5) == 5

def test_multiplication():
    assert multiply(10, 5) == 50

def test_division():
    assert divide(10, 5) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
