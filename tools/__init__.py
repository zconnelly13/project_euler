"""
Commonly used functions in pje problems
"""


from math import sqrt


def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for i, isprime in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False


def divisor_generator(n):
    large_divisors = []
    for i in xrange(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def proper_divisor_generator(n):
    for divisor in divisor_generator(n):
        if divisor < n:
            yield divisor


def quadratic(a, b):
    def quad(n):
        return n**2 + a*n + b
    return quad
