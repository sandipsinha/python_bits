def isprime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n % 5 == 0:
        return False
    elif n % 7 == 0:
        return False

    return True

print 'is 5231 a prime', isprime(5231)

print 'is 77 a prime', isprime(77)
