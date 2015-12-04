"""
Problem 25
==========

The Fibonacci sequence is defined by the recurrence relation:

F(n) = F(n-1) + F(n-2), where F(1) = 1 and F(2) = 1.

The 12th term, F(12), is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence 
to contain 1000 digits?
"""

def fib_generator(limit):
    current = 1
    prev = 1
    yield current
    yield prev
    for i in xrange(0, limit):
        next = current + prev
        prev = current
        current = next
        yield current

for i, n in enumerate(fib_generator(5000)):
    if len(str(n)) == 1000:
        print i+1
        break
