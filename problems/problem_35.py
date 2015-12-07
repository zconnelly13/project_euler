"""
Problem 35
==========

The number, 197, is called a circular prime because all rotations of the digits:
197,
971,
and 719

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 and 97.

How many circular primes are there below one million?
"""

from tools import primes_sieve

primes = {p: True for p in primes_sieve(10000000)}

def circulate(n):
    n = list(str(n))
    circulated = []
    for i in range(len(n)):
        circulated.append(int(''.join(n)))
        n.insert(0, n.pop())
    return circulated

circular_primes = [
    n for n in range(0,1000000)
    if all([
        bool(primes.get(c))
        for c in circulate(n)])]

print len(circular_primes)
