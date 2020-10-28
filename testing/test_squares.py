import pytest
from Programs import squares

def test_list_squares():
    assert squares.list_of_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}



