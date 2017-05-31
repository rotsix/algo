#!/usr/bin/env python

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# +-+-+
# | | |
# +-+-+
# | | |
# +-+-+

# 2×2 grid, but 9 corners (3×3)

MAX = 21

map = [[0] * MAX] * MAX

for i in range(len(map)):
    for j in range(len(map[i])):
        if i == 0 or j == 0:
            map[i][j] = 1
        else:
            map[i][j] = map[i-1][j] + map[i][j-1]

print(map)
print(map[MAX-1][MAX-1])
