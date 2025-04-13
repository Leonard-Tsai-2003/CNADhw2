import pytest
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from factorial import calculate_factorial

def test_factorial_positive_numbers():
    assert calculate_factorial(1) == 1
    assert calculate_factorial(2) == 2
    assert calculate_factorial(5) == 120
    assert calculate_factorial(10) == 3628800

def test_factorial_zero():
    assert calculate_factorial(0) == 1

def test_factorial_negative_numbers():
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
        calculate_factorial(-1)
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
        calculate_factorial(-5) 