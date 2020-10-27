import pytest
from Programs import vowels

def test_num_of_vowels():
    assert vowels.vowels('supercalifragilisticexpialidocious') == 16