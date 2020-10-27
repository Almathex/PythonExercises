import pytest
from Programs import count

def test_count_zeros():
    assert count.count([0,0,0], 0) == 3

def test_count_string():
    assert count.count(["a","a","a"], "a") == 3

def test_count_minus():
    assert count.count([-1, -4, -8, -12],-12) == 1

def test_count_normal_number():
    assert count.count([1, 2, 2, 2, 3, 4, 1, 5, 6], 2) == 3  