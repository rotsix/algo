module Problem040 (answer) where

-- An irrational decimal fraction is created by concatenating the positive integers:
-- 0.12345678910_1_112131415161718192021...

-- It can be seen that the 12th digit of the fractional part is 1.
-- If dn represents the nth digit of the fractional part, find the value of the following expression.
-- d₁ × d₁₀ × d₁₀₀ × d₁₀₀₀ × d₁₀₀₀₀ × d₁₀₀₀₀₀ × d₁₀₀₀₀₀₀

import Utils (int2array)

answer :: Integer
answer = product $ [d!!0, d!!9, d!!99, d!!999, d!!9999, d!!99999]
  where d = concat $ map (reverse . int2array) [1..]
