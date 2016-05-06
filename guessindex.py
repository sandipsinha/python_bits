def sortalg(anarray, uniq):
    ceil = len(anarray) - 1

    floor = 1
    while floor + 1 < ceil:
        #print 'the value of ceil is', ceil, floor
        guess_index = (ceil+floor)/2
        #print 'the guess_index is', guess_index
        if anarray[guess_index] == uniq:
            return guess_index
        elif anarray[guess_index] > uniq:
            ceil = guess_index
        elif anarray[guess_index] < uniq:
            floor = guess_index

    return -1


temparray = [2,5,6,9,12,17,19,30,45,55,87,90]

print 'the number 45 is in temparray', sortalg(temparray, 45)


print 'the number 109 is in temparray', sortalg(temparray, 109)
            
