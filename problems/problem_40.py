"""
Problem 40
==========

An irrational decimal fraction is created by concatenating
the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d(n) represents the nth digit of the fractional part,
find the value of the following expression.

d(1) x d(10) x d(100) x d(1000) x d(10000) x d(100000) x d(1000000)
"""


from operator import mul

digit_indicies = [10**i for i in range(0, 7)]
fraction = ''.join([str(i) for i in range(0, 200000)])

digits = [int(fraction[i]) for i in digit_indicies]
product = reduce(mul, digits)
print product
