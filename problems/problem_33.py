"""
Problem 33
==========

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to
simplify it may incorrectly believe that 49/98 = 4/8, which is carrect, is obtained by cancelling
the 9s.

We shall consider fractions like, 30/50 = 3/5 to be trivial examples

There are exactly four non-trivial examples of this type of fraction, less than one in value,
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the 
denominator.
"""

from fractions import Fraction


def canceled(n, d):
    removed = False
    n = list(str(n))
    d = list(str(d))
    for digit in n:
        if digit in d and digit != '0':
            removed = True
            n.remove(digit)
            d.remove(digit)
    n = int(''.join(n))
    d = int(''.join(d))
    if removed:
        try:
            return (float(n)/float(d))
        except ZeroDivisionError:
            return None
    else:
        return None

fractions = [
    Fraction(n, d)
    for n in range(10,100)
    for d in range(n+1, 100)
    if (float(n)/float(d)) == canceled(n, d)] 

product = reduce(lambda x, y: x*y, fractions)
print product.denominator
