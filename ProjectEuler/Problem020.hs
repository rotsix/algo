module Problem020 (answer) where

-- n! means n × (n − 1) × ... × 3 × 2 × 1

-- For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
-- and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

-- Find the sum of the digits in the number 100!

answer :: Integer
answer = sum $ int2array $ fact 100

fact :: Integer -> Integer
fact 1 = 1
fact n = n * (fact $ n-1)

int2array :: Integer -> [Integer]
int2array n
  | n < 10    = [n]
  | otherwise = n `mod` 10 : (int2array $ n `div` 10)

