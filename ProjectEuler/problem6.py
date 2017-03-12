#!/usr/bin/env python

# The sum of the squares of the first ten natural numbers is,
# 1² + 2² + ... + 10² = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)² = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

each = 0
for i in range(101):
    each += i**2

sum = (100*101)/2
sum *= sum

print(sum - each)
