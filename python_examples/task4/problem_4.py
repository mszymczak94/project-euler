"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
from utils.utils import is_palindrome


def get_biggest_palindrome() -> int:
    first_digits = 999
    biggest_palindrome = -1
    while first_digits > 100:
        second_digits = first_digits
        if second_digits * first_digits < biggest_palindrome:
            break
        while second_digits > 100:
            result = first_digits * second_digits
            if is_palindrome(str(result)) and biggest_palindrome < result:
                biggest_palindrome = result
                break
            second_digits -= 1
        first_digits -= 1
    return biggest_palindrome


print(f'Largest palindrome made from product of two 3-digit numbers is: {get_biggest_palindrome()}')
