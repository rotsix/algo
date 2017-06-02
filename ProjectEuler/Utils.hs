module Utils (rmdup, divisors) where

-- community/haskell-primes
import Data.Numbers.Primes
import Data.List

rmdup :: Ord a => [a] -> [a]
rmdup [] = []
rmdup (x : xs) = x : (rmdup $ filter (\y -> not (x == y)) xs)

divisors :: Integer -> [Integer]
divisors n = map product $ init $ rmdup $ subsequences $ primeFactors n
