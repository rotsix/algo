#!/usr/bin/env python

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from utils import get_divisors

MAX = 28123


def isAbundantSum(x, y):
    if x <= 0 or y >= MAX:
        return False
    return (abundants[x] and abundants[y]) or isAbundantSum(x - 1, y + 1)


isAbundant = lambda n: n < sum(get_divisors(n)) - n
abundants = {n: isAbundant(n) for n in range(1, MAX)}
abundant_sums = {n: False for n in range(1, MAX)}
for i in filter(lambda x: abundants[x], abundants):
    for j in filter(lambda x: abundants[x], abundants):
        if i + j <= MAX:
            abundant_sums[i + j] = True

print(sum(filter(lambda x: not abundant_sums[x], abundant_sums)))
