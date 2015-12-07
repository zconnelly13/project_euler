"""
Problem 4
=========

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import itertools


def is_palindrome(n):
    return str(n) == str(n)[::-1]

three_digit_numbers = range(100, 1000)
largest_palindrome = max(
    [i*j for i, j in
     itertools.product(three_digit_numbers, three_digit_numbers)
     if is_palindrome(i*j)])

print(largest_palindrome)
