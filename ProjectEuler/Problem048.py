#!/usr/bin/env python

# The series, 1¹ + 2² + 3³ + ... + 10¹⁰ = 10405071317.
# Find the last ten digits of the series, 1¹ + 2² + 3³ + ... + 1000¹⁰⁰⁰.

def pretty():
    sum = 0
    
    for i in range(1,1001):
        sum += i**i
    
    print(str(sum)[-10:])

def oneliner():
    print(str(sum([i**i for i in range(1,1001)]))[-10:])

oneliner()
