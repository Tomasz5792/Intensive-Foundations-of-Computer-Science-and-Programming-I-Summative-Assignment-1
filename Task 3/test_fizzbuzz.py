"""
The task is to print numbers from 1 to a given limit, replacing:
Multiples of 3 with "Fizz"
Multiples of 5 with "Buzz"
Multiples of both 3 and 5 with "FizzBuzz"
"""

from main_fizzbuzz import fizzbuzz

def test_fizzbuzz_numbers_correct():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(4) == "4"
    assert fizzbuzz(7) == "7"
    assert fizzbuzz(8) == "8"
    
def test_fizzbuzz_numbers_notcorrect():
    assert fizzbuzz(3) != "3"
    assert fizzbuzz(15) != "15"
    assert fizzbuzz(5) != "5"
    assert fizzbuzz(6) != "6"
    assert fizzbuzz(9) != "9"
    assert fizzbuzz(10) != "10"

def test_fizzbuzz_fizz_correct():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"

def test_fizzbuzz_buzz_correct():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"

def test_fizzbuzz_fizzbuzz_correct():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"