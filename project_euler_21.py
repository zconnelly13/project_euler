"""
Problem 21
==========

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).

If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from tools import proper_divisor_generator


n_to_d_of_n = {}
amicable_numbers = []


# here I use this "n_to_d_of_n" dictionary to avoid computing sum of
# proper divisors more than once, but it's not really a nessecary optimization
for n in range(0, 10000):
    d_of_n = sum(proper_divisor_generator(n))
    n_to_d_of_n[n] = d_of_n
    if n == n_to_d_of_n.get(d_of_n) and n != d_of_n:
        amicable_numbers.extend((n, d_of_n))

print(sum(amicable_numbers))
