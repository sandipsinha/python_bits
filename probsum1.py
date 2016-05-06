def getprob1():
    sum = 0
    for number in xrange(1000):
        if number % 3 == 0 or number % 5 == 0:
            sum += number

    return number

print getprob1()
