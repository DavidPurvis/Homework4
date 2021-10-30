import pytest
from main import *

@pytest.mark.parametrize("name, result", [("testing.txt", None), ("abc.txt", None), (1, None)])
def test_openfile(name, result):
	assert openFile(name) == result
	
@pytest.mark.parametrize("number1, number2, answer", [(5, 1, 5), (30, 5, 6), (5, 0, None)])
def test_numbers(number1, number2, answer):
	assert numbers(number1, number2) == answer

@pytest.mark.parametrize("values, expected", [([0, 0, 5, 5], 7.071068), ([-5.0, -5.0, 5.0, 5.0], 14.142136), ([-55, -57, 100, 100], 220.621848), ([-550, -570, 1000, 1000], 2206.218484), (['a', 'b', 'c', 'd'], None)])
def test_dist(values, expected):
    assert pytest.approx(dist(values[0], values[1], values[2], values[3]), .00001) == expected

@pytest.mark.parametrize("values, bool", [("david", False), (676, True), ("davidivad", True), ([1, 2, 3], False), ([1,2,3,2,1], True)])
def test_isPalindrome(values, bool):
    assert isPalindrome(values) == bool
	
def test_for_sqrt():
	assert sq(9) == 3
	
def test_for_neg_sqrt():
	assert sq(-5) == None
	
def test_for_not_integer():
	assert sq("abc") == None
	
def test_numbersstring():
	assert numbers("hi", "one") == None
	
def test_for_only_string():
	assert greetUser("alexander", "du0ng", "bu1") == None
	
def test_for_greet_user():
	assert greetUser("alexander", "duong", "bui") == None

def test_for_integer():
	assert greetUser(1, 2, 3) == None
	
def genInputs():
	inputs = ["8", "1"]
	
	for item in inputs:
		yield item

GEN = genInputs()
	
def test_divide(monkeypatch):
	monkeypatch.setattr('builtins.input', lambda _: next(GEN))
	assert divide() == None
	
def test_divide2(monkeypatch, capsys):
	monkeypatch.setattr('builtins.input', lambda _: "8")
	divide()
	captured_stdout, captured_stderr = capsys.readouterr()
	assert captured_stdout.strip() == "Your numbers divided is: 1.0"
	
def test_divide2(monkeypatch, capsys):
	monkeypatch.setattr('builtins.input', lambda _: "0")
	divide()
	captured_stdout, captured_stderr = capsys.readouterr()
	assert captured_stdout.strip() == "Please try again"

