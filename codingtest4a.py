def wrapper(func):
    def modicum(*args, **kwargs):
        result = func(*args, **kwargs)
        #print 'first pass', result
        results = [(lambda x: '+' + x[0:2] + ' ' + x[2:7] + ' ' + x[7:])(x) for x in result]
        #print 'second pass', results
        return results
    return modicum

@wrapper
def sortfunction(numly):
    y = [(lambda x: '91' + x if len(x) == 10 and x[0] != '+' else '91' + x[1:] if x[0]=='0' else x[1:] )(x) for x in numly]
    z = sorted(y)
    return z


n=int(raw_input())
numa=[]
for i in xrange(n):
    numa.append(str(raw_input()))
for items in sortfunction(numa):
    print items

