"""
Problem 32
==========

<<<<<<< HEAD
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n
exactly once; for example, the 5-digit number, 15234, is a 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/ multiplier/product identify can be written as a 1
through 9 pandigital.
"""

def is_pandigital(a, b):
    identity = sorted(list(str(a) + str(b) + str(a*b)))
    return (
        identity == sorted(list(set(identity))) 
        and len(identity) == 9
        and '0' not in identity)

pandigital_products = [
    a*b
    for a in range(1000)
    for b in range(1000)
    if is_pandigital(a, b)]

pandigital_products.extend([
    a*b
    for a in range(10)
    for b in range(1000, 10000)
    if is_pandigital(a, b)])

print(sum(set(pandigital_products)))
