module Problem041 (answer) where

-- We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

-- What is the largest n-digit pandigital prime that exists?

import Data.Numbers.Primes
import Data.List
import Utils (int2array, fact)

answer :: Integer
answer = last $ takeWhile (\i -> pandigital i && isPrime i) [2..]
  where 
    pandigital n = (sort $ int2array n) == [1..(toInteger $ length $ int2array n)]
