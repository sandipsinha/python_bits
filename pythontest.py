def trueprime(x,num):
    #print x
    #print num
    if len(x) > 20:
        if num % 7 == 0 or num % 11 == 0 or num % 13 == 0 or num %17 == 0 or num % 3 == 0 or num % 5 == 0 or num % 17 == 0 or num % 19 == 0:
            return False
    for a in x:
        if num % a == 0 and a != 1:
            #print 'The number was found to be ', num, 'And ', a
            return False
    return True    
        


def  getNumberOfPrimes( n):
    x=[]
    for items in xrange(1,n+1,2):
        if len(x) > 1:
            if trueprime(x,items):
                #print 'the number is prime', items
                x.append(items)
            #else:
                #print 'the number is not prime', items
        else:
            x.append(items)            
    #print x        
    return len(x)
##import math
##
##def  getNumberOfPrimes( n):
##    x=math.log(n)
##    return n/(x - 1.08366)

print getNumberOfPrimes(1000000)

