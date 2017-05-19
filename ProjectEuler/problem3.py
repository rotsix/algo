#!/usr/bin/env python

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import *

def isprime(nb):
    global prime
    if nb <= 1: return False
    for elt in prime:
        if nb%elt == 0:
            return False
    return True

prime = []
n = 600851475143

sqr = ceil(sqrt(n))
i = 2
while i <= sqr:
    if isprime(i) is True:
        prime.append(i)
        while n%i == 0:
            n /= i
        sqr = ceil(sqrt(n))
    i += 1

# it only remains the last prime factor
print(int(n))

