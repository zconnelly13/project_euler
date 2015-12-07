"""
Problem 7
=========

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10,001st prime number?
"""


from tools import primes_sieve


for i, j in enumerate(primes_sieve(1000000)):
    if i == 10000:
        print(j)
        break
