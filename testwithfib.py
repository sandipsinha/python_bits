def fib(x):
    a, b = 1, 2
    for items in xrange(1, x):
        a, b = b, a+b
    return a

def actualfib():
    sumarray = []
    i = 1
    while True:
        x = fib(i)
        if x % 2 == 0 and x <= 4000000:
            sumarray.append(x)
        elif x > 4000000:
            break
        i +=1
    return sum(sumarray)    

print 'the test fibx of 7 is ' , actualfib()




