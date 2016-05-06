def is_prime(x):
    if x < 3:
        return False

    for n in range(2, x+1):
        if n == x:
            pass
        elif x%n == 0:
            #print 'I am here', n
            return False

    return True

if __name__=="__main__":
    print 'The number 33 is a prime number', is_prime(33)
    print 'The number 169 is a prime number', is_prime(169)
    print 'The number 37 is a prime number', is_prime(37)
    
    
