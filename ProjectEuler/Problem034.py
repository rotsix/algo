#!/usr/bin/env python

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: As 1! = 1 and 2! = 2 are not sums they are not included.


import math

fact = lambda n: math.prod([d for d in range(1, n + 1)])
digit_fact = lambda n: sum([fact(int(d)) for d in str(n)])


# this gives us the upper limit (10,000,000)
MAX = 9
f = digit_fact(MAX)

while f > MAX:
    MAX = MAX * 10 + 9
    f = digit_fact(MAX)

print(MAX)

# this solution is so ugly
print(sum([n for n in range(MAX) if not print(n) and n == digit_fact(n)]))
