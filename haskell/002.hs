{-
Find the sum of the even-valued terms, for fibonacci numbers under four million.
-}

-- reversive implementation
fibs :: Integer -> Integer
fibs 0 = 1
fibs 1 = 1
fibs n = fibs(n-1) + fibs(n-2)

-- infinite implementation
{-
assume that we have the infinite list of fiboniaci numbers fibs'
zipWith add fibs' and tail of fibs'
prepending 1 and 1 seeds the function 
-}

fibs' :: [Integer]
fibs' = 1:1:zipWith (+) fibs' (tail fibs')

even_fibs' :: [Integer]
even_fibs' = [x | x <- fibs', even x]

main = putStrLn . show . sum $ takeWhile (<4*10^6) even_fibs'