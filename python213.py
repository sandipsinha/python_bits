def getprod(srot,runtot,n):
    if n == 0:
        return 1
    elif n == 1:
        return srot[0]
    else:
        return srot[n-1]*runtot
    
def maxret(slong):
    runtot = 1
    b4prod = []
    n = 0
    for items in slong:
        b4prod.append(getprod(slong,runtot,n))
        runtot = b4prod[-1]
        n += 1
        #print 'runtot is now ' , runtot, n
    return b4prod

if __name__== "__main__":
    a=[1, 2, 6, 5, 9]
    b=[]
    b.extend(a)
    a1 = maxret(a)
    #print 'The orign', a1
    b.reverse()
    #print 'thes result', b
    b1=maxret(b)
    b1.reverse()
    #print 'the reverse', b1
    c=[a*b for a,b in zip(a1,b1)]
    print 'The array is ', c
    
     
    
