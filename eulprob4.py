def is_prime(n):
    print 'the number is ', n
    if n < 3:
        print 'True s'
        return True
    for x in xrange(2,n):
        if n % x == 0:
            print 'false'
            return False
    print 'True'
    return True


def find_smallest_prod(n):
    y = 1
    for x in xrange(2,n+1):
        if is_prime(x):
            y *= x
        print 'y is now ', y , x
    return y

print 'the smallest multiple is', find_smallest_prod(10)
