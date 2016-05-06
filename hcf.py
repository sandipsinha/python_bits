def gcd(a,b):
    while a != b:
        if a > b:
            a -= b
        elif b > a:
            b -= a
    return a

print 'the highest common factor was', gcd(6,8)
