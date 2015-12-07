"""
Problem 43
==========

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""


from itertools import permutations
from tools import primes_sieve

pandigitals = permutations([str(i) for i in range(10)])
primes = list(primes_sieve(20))


def has_substring_divisibility_property(n):
    return all(
        [int(''.join(n[i:i+3])) % primes[i-1] == 0
         for i in range(1, 8)])

pandigitals_with_property = [
    int(''.join(n)) for n in pandigitals
    if has_substring_divisibility_property(n)]

print(sum(pandigitals_with_property))
