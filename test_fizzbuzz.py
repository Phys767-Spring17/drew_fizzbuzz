from fizzbuzz import fizzbuzz
import pytest

def test_fizzbuzz_1():
	assert fizzbuzz(1) == 1

def test_fizzbuzz_3():
	assert fizzbuzz(3) == 'fizz'

def test_fizzbuzz_5():
	assert fizzbuzz(5) == 'buzz'

def test_fizzbuzz_15():
	assert fizzbuzz(15) == 'fizzbuzz'