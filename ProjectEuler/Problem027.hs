module Problem027 (answer) where

-- Euler discovered the remarkable quadratic formula:

-- n²+n+41
-- It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40, 40²+40+41 = 40(40+1)+41 is divisible by 41, and certainly when n=41,41²+41+41 is clearly divisible by 41.

-- The incredible formula n²−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

-- Considering quadratics of the form:

-- n²+an+b, where |a|<1000 and |b|≤1000

-- where |n| is the modulus/absolute value of n
-- e.g. |11|=11 and |−4|=4
-- Find the product of the coefficients, aa and bb, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

import Data.List
import Data.Ord
import Data.Numbers.Primes

answer :: Integer
answer = fst $ maximumBy (comparing . snd) $ takeWhile (isPrime . snd) [(a*b, n^2 + a*n + b) | a <- [-1000..1000], b <- [-1000..1000], n <- [0..]]

-- answer = snd $ maximumBy (comparing $ length) $ takeWhile (isPrime . fst) [((n^2 + n*x + y), x*y) | n <- [0..], x <- [-1000..1000], y <- [-1000..1000]]
-- answer = fst . maximumBy (comparing snd) $ primap (-1000) (-1000)

-- primap :: Integer -> Integer -> [(Integer, Integer)]
-- primap 1001 _ = []
-- primap x y
--  | y < 1000 = ((x * y), fromIntegral $ length $ takeWhile (isPrime) $ map (\i -> i^2 + i*x + y) [0..]) : primap x (y+1)
--  | y == 1000 = ((x * y), fromIntegral $ length $ takeWhile (isPrime) $ map (\i -> i^2 + i*x + y) [0..]) : primap (x+1) (-1000)


