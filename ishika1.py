def isdivisibleby9(theNum):
    if theNum%9 == 0:
        print theNum
        return 1
    else:
        return 0
count = 0    
for x in xrange(400,601):
    count += isdivisibleby9(x)
    
print 'The number of numbers between 400-600 which are' \
      ' divible by 9 are {}'.format(count)
    
    
