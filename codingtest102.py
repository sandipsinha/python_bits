n=int(raw_input())
numa=[]
for i in xrange(n):
    numa.append(int(raw_input()))
print numa
start = 0
uniques=set(numa)
testa=list(uniques)
for indx, items in enumerate(testa):
    if indx+2 <= len(testa)-1:
        if items + 1 == testa[indx+1] and  testa[indx+1] + 1 == testa[indx+2]:
            if numa.count[items] == numa.count[ testa[indx+1]] and
                numa.count[ testa[indx+1]] == numa.count[ testa[indx+2]]:
                    return true
            elif numa.count[items] == numa.count[ testa[indx+2]] and
                numa.count[ testa[indx+1]] >= numa.count[ items]:
                    return true
return False
                
            
            
