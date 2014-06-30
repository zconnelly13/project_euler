n = 600851475143
i = 2
prime_factors = []
# it's not going to have a factor larger than sqrt(n)
while i*i < n:
    # if i is a factor of n
    while n % i == 0:
        # a prime factor is found
        prime_factors.append(i)
        # divide by that prime factor
        n = n / i
    i = i+1
# the "n" leftover may also be a prime factor if not 1
if n > 1:
    prime_factors.append(n)

largest = max(prime_factors)
print largest
