def fibon(n):
##    a = b = 1
##    for i in range(n):
##        yield a
##        a, b = b, a + b
    if n <= 2:
        return 1
    else:
        return fibon(n-1) + fibon(n-2)
    
print fibon(8)
