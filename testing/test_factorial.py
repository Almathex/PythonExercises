import pytest
from Programs import factorial 

def test_factorial():
    assert factorial.fact(5) == 120

