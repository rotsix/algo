module Problem023 (answer) where

import Utils (divisors)

answer :: Integer
answer = sum [i | i <- [1..28123], not $ isAbundantSum (floor $ (fromIntegral i)/2) (ceiling $ (fromIntegral i)/2)]


abundant :: Integer -> Bool
abundant n = n > (sum $ divisors n)

isAbundantSum :: Integer -> Integer -> Bool
isAbundantSum 0 _ = False
isAbundantSum _ 0 = False
isAbundantSum x y = (abundant x && abundant y) || isAbundantSum (x-1) (y+1)
