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
