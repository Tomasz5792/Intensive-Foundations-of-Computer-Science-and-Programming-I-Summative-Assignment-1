"""
The task is to print numbers from 1 to a given limit, replacing:
Multiples of 3 with "Fizz"
Multiples of 5 with "Buzz"
Multiples of both 3 and 5 with "FizzBuzz"
"""

from main_fizzbuzz import fizzbuzz

def test_fizzbuz_passes():
    assert fizzbuzz(1) == True