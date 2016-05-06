def fib(n):
    x={}
    if n < 2:
        return n
    if n in x:
        return x[n]
    else:
        x[n] = fib(n-1)+fib(n-2)
        return x[n]


print 'fib of 4 is', fib(4)
