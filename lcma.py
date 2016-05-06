from fractions import gcd
def getlcm(x,y):
    return x*y//gcd(x,y)
    

def lacm(x):
    n = 1
    y = [number for number in xrange(1, x+1)]
    z = reduce(getlcm, y)
    return z

print 'the lacm of 20 is', lacm(20)
print 'the lacm of 10 is', lacm(10)
        
    
    
