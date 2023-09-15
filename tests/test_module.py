import pytest
from my_project.math_operations import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_mixed_numbers():
    assert add(-1, 1) == 0

@pytest.mark.parametrize("a, b, expected", [(0, 0, 0), (1, 0, 1), (0, 1, 1)])
def test_add_with_zero(a, b, expected):
    assert add(a, b) == expected

