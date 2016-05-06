def findmax(word1, word2):
    words1 = set(word1)
    words2 = set(word2)
    if len(words1.intersection(words2)) > 0:
        if len(word1)>len(word2):
            return word1
        else:
            return word2
    else:
        return  len(word1)*len(word2)


def GetMaxItems(thearray):
    thearray = sorted(thearray, key=lambda x:len(x), reverse=True)
    for indx, items in enumerate(thearray):
        if indx >= 2:
            theret = findmax(thearray[indx-2],thearray[indx-1])
            if isinstance(theret, int):
                return theret

    return findmax(thearray[indx],thearray[indx-1])
 


thedata = ['ABCW', 'BAZ', 'FOO', 'BAR', 'XTFN','ABCDEF']
print GetMaxItems(thedata)

                
                    
            
        
        
        
