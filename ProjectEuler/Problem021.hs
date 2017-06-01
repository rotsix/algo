module Problem021 (answer) where

-- Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
-- If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

-- For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

-- Evaluate the sum of all the amicable numbers under 10000.

-- community/haskell-primes
import Data.Numbers.Primes
import Data.List
import Data.Tuple

answer :: Integer
answer = sum [i | i <- [2..10000], isAmicable i]
  where
    -- isAmicable if (amicable $ amicable n) == n and (amicable n ≠ n)
    isAmicable n = let an = amicable n in (n /= an) && (amicable an == n)
    -- amicable n = sum of the divisors of n
    amicable n = sum $ map product $ init $ rmdup $ subsequences $ primeFactors n

rmdup :: Ord a => [a] -> [a]
rmdup [] = []
rmdup (x : xs) = x : (rmdup $ filter (\y -> not (x == y)) xs)

