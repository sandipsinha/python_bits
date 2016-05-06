def kist(d):
    l=[]
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < d[i]] or [[]], key=len) + [d[i]])
    print 'the array is ', l

    return max(l, key=len)

print kist([3,2,6,4,5,1])
