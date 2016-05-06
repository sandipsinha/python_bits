def fib2(n):
    if n <= 2:
        return 1
    return fib2(n-1) + fib(n-2)


def fib(n):
    a,b = 0,1
    for i in range(n-1):
        a,b=b,a+b
    return b

print 'the fibd of 100 is.', fib(100)
print 'the verify fibd of 7 is.', fib2(7)

print 'the fib of 20 is', fib(8)
print 'the very fib of 20 is', fib2(8)
