def sfind(n):
    atta = []
    xy = ''
    for items in n:
        #print 'Now reading', items
        if items == '0':
            xy = xy + '0'
        elif len(xy) > 0:
            atta.append(xy)
            xy = ''
    if len(xy) > 0:
        atta.append(xy)
    return len(sorted(atta, key=len, reverse=True)[0])

print 'the maximum distance of binary 12 is', bin(1041)

print sfind(str(bin(1041)))
            
            
            
