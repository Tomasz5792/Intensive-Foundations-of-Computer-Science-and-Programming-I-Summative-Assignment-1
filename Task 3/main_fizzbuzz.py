"""
The task is to print numbers from 1 to a given limit, replacing:
Multiples of 3 with "Fizz"
Multiples of 5 with "Buzz"
Multiples of both 3 and 5 with "FizzBuzz"
"""

def fizzbuzz(number: int) -> str:
    """
    plays the fizz buzz game

    Args:
        number (int): the number to fizzbuzz

    Returns:
        str: the string Fizz Buzz FizzBuzz or the number

    Raises:
        ValueError: number should be an integer
    """

    if not isinstance(number, int):
        raise ValueError("number should be an integer")

    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"

    if number % 3 == 0:
        return "Fizz"
    
    if number % 5 == 0:
        return "Buzz"

    return str(number)

