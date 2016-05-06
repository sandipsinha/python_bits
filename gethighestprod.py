def gethighestprod(inptarray):
    highestprodoftwo = inptarray[0]*inptarray[1]
    lowestprodoftwo = inptarray[0]*inptarray[1]
    highestprodofthree = inptarray[0]*inptarray[1]*inptarray[2]
    maxnum = inptarray[0]
    minnum = inptarray[0]
    for index, number in enumerate(inptarray):
        maxnum = max(maxnum, number)
        minnum = min(minnum, number)
        if index < len(inptarray) -2 :
            highestprodoftwo = max(highestprodoftwo, maxnum * inptarray[index+1])
            highestprodoftwo = max(highestprodoftwo, minnum * inptarray[index+1])
            lowestprodoftwo = min(lowestprodoftwo, minnum * inptarray[index+1])
            lowestprodoftwo = min(lowestprodoftwo, maxnum * inptarray[index+1])
            highestprodofthree = max(highestprodofthree, highestprodoftwo * inptarray[index+2])
            highestprodofthree = max(highestprodofthree , lowestprodoftwo * inptarray[index+2])

            

    return highestprodofthree


thelist = [1, 10, -5, 1, -100, -3,10,-200]
print 'The highest prod is', gethighestprod(thelist)
                                     
            
