module Problem035 (answer) where

-- The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
-- There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
-- How many circular primes are there below one million?

import Data.Numbers.Primes
import Data.List
import Utils (int2array, array2int)

answer :: Integer
answer = toInteger $ length $ filter (\x -> x < 1000000 && (circular $ int2array x)) primes
  where circular n = length n == (length $ filter (isPrime) [array2int i | i <- permutations n])
