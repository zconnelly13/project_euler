"""
Problem 30
==========

Surprisingly there are only three numbers that can be written as the sum
of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the
sum of fifth powers of their digits.
"""

upper_bound = 1000000
power = 5


def sum_power_of_digits(n, power):
    return sum([int(d)**power for d in str(n)])

expressable_as_fifth_powers_of_digits = [
    n for n in xrange(2, upper_bound)
    if n == sum_power_of_digits(n, power)]

print(sum(expressable_as_fifth_powers_of_digits))
