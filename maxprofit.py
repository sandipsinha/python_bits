def findbestprice(thearay):

    minprice = thearray[0]
    maxprofit = 0

    for currentprice in thearray:
        minprice = min(currentprice, minprice)
        maxprofit = max(maxprofit, currentprice-minprice)

    return maxprofit

thearray = [10, 7, 5, 8, 11, 9]

print 'the best price is', findbestprice(thearray)
