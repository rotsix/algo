module Utils (rmdup, divisors, int) where

-- community/haskell-primes
import Data.Numbers.Primes
import Data.List

-- remove duplicates : [[1,3], [1,3], [2,2]] -> [[1,3], [2,2]]
rmdup :: Ord a => [a] -> [a]
rmdup [] = []
rmdup (x : xs) = x : (rmdup $ filter (\y -> not (x == y)) xs)

-- list of divisors : 28 -> [2, 2, 7]
divisors :: Integer -> [Integer]
divisors n = map product $ init $ rmdup $ subsequences $ primeFactors n

-- array to integer : [1, 2, 3] -> 123
int :: Integer -> [Integer] -> Integer
int _ [] = 0
int n (x : xs) = (10^n)*x + (int (n+1) xs)
