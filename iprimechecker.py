def isPrime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for n in xrange(3,x, 2):
        if x % n == 0:
            return False
    return True

x = 3
counter = 2

while True:
    x += 2
    if isPrime(x):
        counter += 1
        if counter == 10001:
            print 'The 10001 prime number is %d'%(x)
            break
        

        
        
        
