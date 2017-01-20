#!/usr/bin/env python

l = [1,2,3]

s = 1+2+3
while l[2] < 4_000_000:
    l[2] = l[1] + l[0]
    l[0] = l[1]
    l[1] = l[2]
    s = s+l[2]
    print(l[2])

print(s)
