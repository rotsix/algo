#!/usr/bin/env python

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import *

def isprime(nb):
    for i in range(3, nb):
        if n%i == 0:
            return False
    return True

prime = []
n = 600851475143

print("Calculating primes")
for i in range(floor(sqrt(n))):
    if isprime(i) is True:
        prime.append(i)

l = [0] * len(prime)

print("division")
while n > 1:
    for i in range(len(prime)):
        while n%prime[i] != 0:
            n /= prime[i]
            l[i] += 1

print("Final multiplication")
res = 1
for i in range(len(l)):
    if l[i] == 0:
        l.pop(i)
        i -= 1

print("res : " + str(l[len(l)-1]))


