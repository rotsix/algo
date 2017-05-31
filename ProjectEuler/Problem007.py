#!/usr/bin/env python

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

primes = []

i = 2
while len(primes) < 10001:
    prime = True
    for elt in primes:
        if i%elt == 0:
            prime = False
            break
    if prime is True:
        primes.append(i)
    i += 1

print(primes[-1])
