import pytest
from Programs import best_conjugation

def test_best_conjugation():
    assert best_conjugation.sorting(best_conjugation.best_conjug("Superman")) == ['super', 'perm', 'sup', 'per', 'man', 'up', 'su', 'pe', 'ma', 'er', 'an']