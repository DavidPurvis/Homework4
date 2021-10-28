import pytest
from main import *

def test_openfile():
	assert openFile("testing.txt") == None
	
def test_openfileNA():
	assert openFile("abc.txt") == None
	
def test_openfileNA2():
	assert openFile(1) == None
	
@pytest.mark.parametrize("number1, number2, answer", [(5, 1, 5), (30, 5, 6)])
def test_numbers(number1, number2, answer):
	assert numbers(number1, number2) == answer

@pytest.mark.parametrize("values, expected", [([0, 0, 5, 5], 7.071068), ([-5.0, -5.0, 5.0, 5.0], 14.142136), ([-55, -57, 100, 100], 220.621848), ([-550, -570, 1000, 1000], 2206.218484), (['a', 'b', 'c', 'd'], None)])
def test_dist(values, expected):
    assert pytest.approx(dist(values[0], values[1], values[2], values[3]), .00001) == expected

@pytest.mark.parametrize("values, bool", [("david", False), (676, True), ("davidivad", True), ([1, 2, 3], False), ([1,2,3,2,1], True)])
def test_isPalindrome(values, bool):
    assert isPalindrome(values) == bool
	
def test_numbersby0():
	assert numbers(5, 0) == None
	
def test_for_sqrt():
	assert sq(9) == 3
	
def test_for_neg_sqrt():
	assert sq(-5) == None
	
def test_for_not_integer():
	assert sq("abc") == None
	
def test_numbersstring():
	assert numbers("hi", "one") == None
