def insertion_sort(thearray):
    for indx,number in enumerate(thearray):
        if indx >= 1:
            for rownum,item in enumerate(thearray[0:indx]):
                if rownum > 0:
                    if thearray[rownum] < thearray[rownum-1]:
                        thearray[rownum-1], thearray[rownum]= thearray[rownum], thearray[rownum-1]


    return thearray



thearray = [54,26,93,17,77,31,44,55,20]

print insertion_sort(thearray)
                    
        
