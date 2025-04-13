import pytest
from odd_even import check_odd_even

def test_odd_numbers():
    assert check_odd_even(1) == "Odd"
    assert check_odd_even(3) == "Odd"
    assert check_odd_even(-1) == "Odd"
    assert check_odd_even(-3) == "Odd"

def test_even_numbers():
    assert check_odd_even(2) == "Even"
    assert check_odd_even(4) == "Even"
    assert check_odd_even(-2) == "Even"
    assert check_odd_even(-4) == "Even"

def test_zero():
    assert check_odd_even(0) == "Even" 