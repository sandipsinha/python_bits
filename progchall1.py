def iseven(x):
    if x % 2 == 0:
        return True
    else:
        return False


def findseries(n1,n2):
    oddnum = 0
    evennum = 0
    i = n1
    m = n2
    y = 0
    maxcycle = 0
    while i < m+1:
        y = i
        #print 'the value of n is now', y
        while y > 1:
            if iseven(y):
                y = y / 2
                evennum +=1
            else:
                y = 3 * y + 1
                oddnum += 1
            #print 'the value of n is now', y
        currentcycle =  oddnum + evennum + 1
        maxcycle = max(maxcycle, currentcycle)
        oddnum = 0
        evennum = 0
        i += 1
    print m , n1, maxcycle

##def findseries(n1,n2):
##    oddnum = 0
##    evennum = 0
##    i = n1
##    m = n2
##    y = n2
##
##    print 'the value of n is now', y
##    while y > 1:
##        if iseven(y):
##            y = y / 2
##            evennum +=1
##        else:
##            y = 3 * y + 1
##            oddnum += 1
##        #print 'the value of n is now', y    
##    print oddnum + evennum 
##    i += 1
##    print m , n1, oddnum + evennum + 1

    
    
print findseries(900, 1000)
