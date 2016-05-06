def newfib(n):
    a,b=0,1
    for x in xrange(n):
        a,b=b,a+b

    return a


print 'the nth fib number is', newfib(100)
