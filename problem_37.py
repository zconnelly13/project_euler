"""
Problem 37
==========

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""


from tools import primes_sieve

upper_limit = 1000000
primes = {p: True for p in primes_sieve(upper_limit)}


def get_truncated(n):
    """
    Returns a unique list of n and all of its truncated versions
    both from the left and the right
    """

    truncated_versions = [n]
    for i in range(1, len(str(n))):
        truncated_versions.append(int(str(n)[i:]))
        truncated_versions.append(int(str(n)[:(-1)*i]))
    truncated_versions = list(set(truncated_versions))
    return truncated_versions

truncatable_primes = []
for n in range(10, upper_limit):
    truncated = get_truncated(n)
    if all([primes.get(p) for p in truncated]):
        truncatable_primes.append(n)

print(sum(truncatable_primes))
