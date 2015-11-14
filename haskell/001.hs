{-
Find the sum of all the multiples of 3 or 5 below 1000.
-}

sum' a b = let _b = (b-1) `quot` a in ((a*_b) * (_b+1)) `quot` 2

main = putStrLn $ show $ sum' 3 1000 + sum' 5 1000 - sum' 15 1000