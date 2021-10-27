import pytest

from main import dist, isPalindrome

"""def test_openfile():
    assert

def test_numbers():
    assert
"""

# def test_dist():
#     assert dist(0, 0, 5, 5) == 7.071068

@pytest.mark.parametrize("values, bool", [("david", False), (676, True), ("davidivad", True), ([1, 2, 3], False)])
def test_isPalindrome(values, bool):
    assert isPalindrome(values) == bool

""" def test_divide():
    assert

def test_sq():
    assert

def test_greetUser():
    assert

def test_displayItem():
    assert
"""