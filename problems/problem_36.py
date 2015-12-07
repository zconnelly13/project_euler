"""
Problem 36
==========

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

upper_bound = 1000000


def is_palindrome(n):
    return str(n) == str(n)[::-1]

dual_palindromes = [
    n
    for n in range(0, upper_bound)
    if is_palindrome(n) and is_palindrome(bin(n)[2:])]

print(sum(dual_palindromes))
