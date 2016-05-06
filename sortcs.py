import collections
def countrepeat(w):
    x = collections.Counter(w)
    wc = 0
    #print w
    #print x
    for items in x.items():
        #print 'items ', items[1]
        wc += 1 if items[1] > 1 else 0
        #print wc
    #print wc    
    return wc, w
        

a = 'ami jaani jee amiiii bokaaaa kintuuuuu ki je korrrrrriiiii'
lv = map(countrepeat, a.split())
mn = sorted(lv, key=lambda x:x[0], reverse=True)
print mn[0][0], 'and ', mn[0][1]
