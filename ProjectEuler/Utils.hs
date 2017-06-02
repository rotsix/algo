module Utils (rmdup, divisors, int, fibo) where

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

-- array to integer : [3, 2, 1] -> 123
int :: Integer -> [Integer] -> Integer
int _ [] = 0
int n (x : xs) = (10^n)*x + (int (n+1) xs)

-- nth fibo term : fibo 3 1 1 ->
-- 1 1 are init terms
-- fibo 2 x _ because of 2 init terms
fibo :: [Integer]
fibo = 1 : 1 : zipWith (+) fibo (tail fibo)

-- fibo :: Integer -> Integer -> Integer
-- fibo x _ 2 = x
-- fibo x y n = (x+y) x (n-1)
