def getproduct(datarray):
    n = 1
    for items in datarray:
        n *= items
    return n

def highestprod(thearray):
    xray = []

    for index, items in enumerate(thearray):
        #print 'the index is now', index
        beforeprod = 1
        afterprod = 1
        if index > 0:
            #print 'the array before is', thearray[0:index]
            beforeprod = getproduct(thearray[:index])
        if len(thearray)-1 >= index+1:
            #print 'the array after is', thearray[index+1:]
            afterprod = getproduct(thearray[index+1:])
        xray.append(beforeprod*afterprod)
    return xray
datarray = [1, 7, 3, 4]
print 'the given prod would be %s',highestprod(datarray)
                                       
            
            
    

    
        
