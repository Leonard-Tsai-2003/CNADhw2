import pytest
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from addition import add_numbers

def test_add_positive_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(10, 20) == 30

def test_add_negative_numbers():
    assert add_numbers(-2, -3) == -5
    assert add_numbers(-10, 5) == -5

def test_add_zero():
    assert add_numbers(0, 0) == 0
    assert add_numbers(5, 0) == 5
    assert add_numbers(0, -3) == -3

def test_add_floats():
    assert add_numbers(1.5, 2.5) == 4.0
    assert add_numbers(-1.5, 1.5) == 0.0 