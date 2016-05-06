from fractions import gcd
def hcf(a,b):
    while a!= b:
        if a > b:
            a -= b
        elif b > a:
            b -= a
    return a

def lcm(*numbers):
    """Return lowest common multiple."""    
    def lcm(a, b):
        #print 'the two numbers are', a, b
        return (a * b) // hcf(a, b)
    return reduce(lambda x,y: lcm(x,y), *numbers)


x = [int(number) for number in xrange(1,21)]
print 'the list is', x
print 'the lcm of numbers 1-20 is',lcm(x)

