"""
Problem 3
=========

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


n = 600851475143
i = 2
prime_factors = []
while i*i < n:
    while n % i == 0:
        prime_factors.append(i)
        n = n / i
    i = i+1
if n > 1:
    prime_factors.append(n)

largest = max(prime_factors)
print(largest)
