import System.Environment (getArgs)

import Control.Monad (liftM)

import Problem003 as P3
import Problem012 as P12
import Problem014 as P14
import Problem020 as P20
import Problem021 as P21
import Problem023 as P23
import Problem024 as P24

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
sol 23 = return $ show P23.answer
sol 24 = return $ show P24.answer
sol _ = return $ show "This problem isn't solved using Haskell"
