def isprime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n % 5 == 0:
        return False
    elif n % 7 == 0:
        return False
    for i in xrange(2, n):
        if n % i == 0:
            return False

    return True


def find_largest_prime(n):
    #print 'Now trying to find factors for ', n
    div = 'n'
    maxvalue = []
    for j in xrange(3,n-1,2):
        if n % j == 0:
            div = 'y'
            break
    if div == 'n':
        #print 'returned value is', n
        return n
    else:
        maxvalue.append(find_largest_prime(n/j))

    return max(maxvalue)
        
     
            
 

 

print 'the largest prime factor is', find_largest_prime(8462696833)

