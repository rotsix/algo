module Problem039 (answer) where

-- If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

-- {20,48,52}, {24,45,51}, {30,40,50}

-- For which value of p ≤ 1000, is the number of solutions maximised?

import Data.List
import Data.Ord

answer :: Integer
answer = fst $ maximumBy (comparing $ snd) $ zip [1..] $ map perimeter [3..1000]

perimeter :: Integer -> Integer
perimeter n = 42


{-



-- calculate nb of 
--      a       -> b       -> c       -> nb
sols :: Integer -> Integer -> Integer -> Integer
sols a b c
  | (a^2 + b^2) == c^2    = (+) 1 $ sols (a+1) b c
  | b > c                 = 0
  | a > b                 = sols 1 (b+1) c
  | otherwise             = sols (a+1) b c

-}
