def cube_root(n):
    "A modified Newton's Method solver for integral cube roots."
    if int(n) != n:
        raise ValueError("must provide an integer")
    if n in (-1,0,1): return n
    offset = (1,-1)[n > 0]
    x = n/2
    seen = set()
    steps = 0
    while 1:
        y = x**3
        if y == n:
            #~ print "Found %d ^ 1/3 = %d in %d steps" % (n,x,steps)
            return x
        dydx = 3.0*x*x
        x += int((n-y)/dydx)+offset
        x = x or 1
        if x in seen:
            raise ValueError("%d is not a perfect cube" % n)
        seen.add(x)
        steps += 1


##def is_perfect_cube(x):
##    x = abs(x)
##    return int(round(x ** (1. / 3))) ** 3 == x
##
##
##print(is_perfect_cube(64))

print 'The Cube root is ' , cube_root(64)

print 'The Cube root is ' , cube_root(13)
