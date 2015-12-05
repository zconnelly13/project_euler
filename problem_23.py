"""
Problem 23
==========

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.
"""

"""
#Notes

Originally I did something like...

```
expressable_as_sums = [
    n for n in range(0, upper_limit)
    if n not in 
    [x + y for x in abundant_numbers for y in abundant_numbers]]
```

But this was hella slow and oomed : /
"""

from tools import proper_divisor_generator


upper_limit = 28123

abundant_numbers = [n for n in range(0, upper_limit)
                    if n < sum(proper_divisor_generator(n))]
abundant_numbers_reversed = abundant_numbers[::-1]

not_expressable_as_sum = range(0, upper_limit+1)
for x in xrange(0, len(abundant_numbers)):
    for y in xrange(0, len(abundant_numbers_reversed)):
        n1 = abundant_numbers[x]
        n2 = abundant_numbers_reversed[y]
        if n1 + n2 <= upper_limit:
            not_expressable_as_sum[n1 + n2] = 0
        else:
            continue
    if n1 + n2 > upper_limit:
        continue

print sum(not_expressable_as_sum)

