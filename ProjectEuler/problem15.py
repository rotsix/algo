#!/usr/bin/env python

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

def dest(x, y, max):
    print(f" x:{x} y:{y}")
    if x == max and y == max:
        return 1
    if x == max:
        return dest(x, y+1, max)
    if y == max:
        return dest(x+1, y, max)
    return dest(x+1, y, max) + dest(x, y+1, max)

print(dest(0, 0, 20))
