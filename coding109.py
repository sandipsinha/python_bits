import math
def fibnaci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibnaci(n-1) + fibnaci(n-2)



x = int(raw_input())
y =[int(math.pow(fibnaci(num),3)) for num in xrange(x)]

print y
