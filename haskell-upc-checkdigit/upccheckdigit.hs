{-- calculates the check digit of a UPC --}


class Upc a where
  isValid :: a -> Bool


-- returns a list of even index elements
evenelems :: [a] -> [a]
evenelems (x:y:ys) = [y]++evenelems(ys)
evenelems (x:xs) = []
evenelems [] = []

-- returns a list of odd index elements
oddelems :: [a] -> [a]
oddelems (x:y:ys) = [x]++oddelems(ys)
oddelems (x:xs) = []
oddelems [] = []


-- returns the check digit of a UPC
-- x is formatted as [1,2,3 ... ]
-- length x == 11
listcheckdigit :: Integral a => [a] -> a
listcheckdigit x =
  let
    evensum = (foldl1 (+) (oddelems x))
    oddsum = (foldl1 (+) (evenelems x))
    checkdigit = mod (evensum * 3 + oddsum) 10
  in
    if checkdigit /= 0 then
      10 - checkdigit
    else
      checkdigit

-- test data
-- y = [0,2,6,2,2,9,5,7,0,7,0]





