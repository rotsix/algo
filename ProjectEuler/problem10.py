#!/usr/bin/env python

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from math import *

def isprime(i):
    if str(i)[-1] == 5:
        return False
    if i <= 1:
        return False
    for elt in prime:
        if elt > sqrt(i):
            return True
        if i%elt == 0:
            return False
    return True

prime = [2,3,5,7]

res = 2+3+5+7
for i in range(11, 2000000, 2):
    if isprime(i) is True:
        prime.append(i)
        res += i
print(res)
