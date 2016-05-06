def findorderset(thearray, thekey):
    ceiling = len(thearray)
    floor = -1 
    

    while floor + 1 < ceiling :
       guess_index = (ceiling+floor)/2 
       guess_number = thearray[guess_index]
       if guess_number == thekey:
           return guess_index
       elif guess_number > thekey:
           ceiling = guess_index
       elif guess_number < thekey:
           floor = guess_index
    return -1


a=[1,4,6,7,8,9,12,13,19,20,21,23,28,39,43,45]           
print findorderset(a,78)    
    
