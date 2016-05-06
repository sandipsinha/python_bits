def findindex(array, val, pos):
    if len(array) == 0:
        return 0

    mid = len(array)/2 + 1
    ceil = len(array)
    
    #print 'The array is ', array , 'and', mid, 'and', pos
    if array[mid] == val:
        return mid + pos
    elif array[mid] > val:
        return findindex(array[0:mid],val, pos) 
    elif array[mid] < val:
        pos += len(array)/2 + 1
        #print 'I am not returning the later half', array[mid:ceil],'*', pos
        return findindex(array[mid:ceil],val, pos)



onesucharray=[2,4,7,8,9,12,13,18, 19,20, 34, 35, 36, 38, 43, 46, 49, 53, 59, 61, 73, 79, 81]
print 'The value of 49 is', findindex(onesucharray, 49, 0)  
print 'The value of 34 is', findindex(onesucharray, 36, 0)

print 'The value of 34 is', findindex(onesucharray, 9, 0)
    
