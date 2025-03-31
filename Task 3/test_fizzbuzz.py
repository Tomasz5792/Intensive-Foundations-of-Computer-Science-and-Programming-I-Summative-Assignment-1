"""
The task is to print numbers from 1 to a given limit, replacing:
Multiples of 3 with "Fizz"
Multiples of 5 with "Buzz"
Multiples of both 3 and 5 with "FizzBuzz"
"""

from main_fizzbuzz import fizzbuzz

def test_fizzbuzz():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(4) == "4"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(7) == "7"
    assert fizzbuzz(8) == "8"
    assert fizzbuzz(15) == "FizzBuzz"