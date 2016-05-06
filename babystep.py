from collections import Counter

def removenum(high, freq, sometuple):
    kenapple = []
    for items in sometuple:
        q, r = items
        if q != high and r != high:
            kenapple.append(items)
    return tuple(kenapple)

def makelist(sometuple):
    somearray = []
    for items in sometuple:
        a, b = items
        #print items, 'and', a ,'*', b
        somearray.append(a)
        somearray.append(b)
        #print 'array', somearray
    return Counter(somearray).most_common(1)


lem = ({1,2},{2,3},{3,4},{4,5},{4,6},{6,5})
r = 0
while len(lem) > 0:
    kano = makelist(lem)
    print 'kano', kano[0]
    high, freq = kano[0]
    lem = removenum(high, freq, lem)
    r += 1
print 'The optinum number is' , r
        

    
