def spitoutsentence(thenumber):
    ansarray = []
    for x in xrange(0,thenumber+1):
        ansarray.append(list(str(bin(x)).strip('0b')).count('1'))

    return ansarray

print 'The answer for number 100 is ' , spitoutsentence(100)
    
