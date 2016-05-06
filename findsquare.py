def findsqrt(x):
    estimate = (1+ x)/2
    new_estimate = 1
    while new_estimate != estimate:
        estimate = new_estimate
        new_estimate = (estimate + x/estimate)/2.0
        print 'tne new estimate is ', new_estimate

    return estimate

print 'The quare root of 9 is', findsqrt(9)

print 'The quare root of 9 is', findsqrt(3)
        
    
