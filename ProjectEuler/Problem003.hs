module Problem003 (answer) where

-- The prime factors of 13195 are 5, 7, 13 and 29.
-- What is the largest prime factor of the number 600851475143 ?

-- community/haskell-primes
import Data.Numbers.Primes

answer :: Integer
answer = last $ primeFactors 600851475143

