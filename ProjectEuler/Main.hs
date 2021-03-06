import System.Environment (getArgs)

import Control.Monad (liftM)

import Problem003 as P3
import Problem012 as P12
import Problem014 as P14
import Problem020 as P20
import Problem021 as P21
import Problem024 as P24
import Problem025 as P25
import Problem027 as P27
import Problem029 as P29
import Problem030 as P30
import Problem035 as P35
import Problem039 as P39
import Problem040 as P40
import Problem041 as P41

main :: IO ()
main = do
  args <- getArgs
  case args of
    [x] -> sol (read x) >>= putStrLn
    _ -> print usage

usage :: String
usage = "Main <problem's number>"

sol :: Int -> IO String
sol 3 = return $ show P3.answer
sol 12 = return $ show P12.answer
sol 14 = return $ show P14.answer
sol 20 = return $ show P20.answer
sol 21 = return $ show P21.answer
sol 24 = return $ show P24.answer
sol 25 = return $ show P25.answer
sol 27 = return $ show P27.answer
sol 29 = return $ show P29.answer
sol 30 = return $ show P30.answer
sol 35 = return $ show P35.answer
sol 39 = return $ show P39.answer
sol 40 = return $ show P40.answer
sol 41 = return $ show P41.answer
sol _ = return $ show "This problem isn't solved using Haskell"
