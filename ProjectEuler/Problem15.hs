module Problem15 (answer) where

-- Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
-- How many such routes are there through a 20×20 grid?

answer :: Integer
answer = roads 20 20

roads :: Integer -> Integer -> Integer
roads 0 0 = 1
roads x 0 = roads (x-1) 0
roads 0 y = roads 0 (y-1)
roads x y = roads (x-1) y + roads x (y-1)
