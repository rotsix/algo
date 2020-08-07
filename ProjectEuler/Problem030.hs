module Problem030 (answer) where

-- Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

-- 1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴
-- 8208 = 8⁴ + 2⁴ + 0⁴ + 8⁴
-- 9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴
-- As 1 = 1⁴ is not a sum it is not included.

-- The sum of these numbers is 1634 + 8208 + 9474 = 19316.

-- Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import Utils (int2array)

answer :: Integer
answer = sum $ trues $ map (\i -> (i, isSum 5 i)) [2..1000000]
  where isSum b a = a == (sum $ map (^b) $ int2array a)

trues :: [(Integer, Bool)] -> [Integer]
trues [] = []
trues (x:xs)
  | snd x == True = (fst x) : trues xs
  | otherwise     = trues xs
