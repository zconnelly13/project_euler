"""
Problem 41
==========

We shall say that an n-digit number is pandigital if
it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""


from tools import primes_sieve
from tools import is_pandigital


# 9 and 8 pandigitals are not prime because
# sum(range(0, 10)) == 45 and 45 % 3 == 0
# and similarly
# sum(range(0, 9)) == 36 and 36 % 3 == 0
upper_bound = 7654321

pandigital_primes = [
    prime for prime in primes_sieve(upper_bound)
    if is_pandigital(prime)]
print max(pandigital_primes)
