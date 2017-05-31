import System.Environment (getArgs)

import Control.Monad (liftM)

import Problem3 as P3
import Problem12 as P12
import Problem14 as P14

main :: IO ()
main = do
  args <- getArgs
  case args of
    [x] -> runSolution (read x) >>= putStrLn
    _ -> print usage

usage :: String
usage = "Main <problem's number>"

runSolution :: Int -> IO String
runSolution 3 = return $ show P3.answer
runSolution 12 = return $ show P12.answer
runSolution 14 = return $ show P14.answer
runSolution _ = return $ show "This problem isn't solved using Haskell"
