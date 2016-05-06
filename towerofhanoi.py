def towerofhanoi(n,src,dest,temp):
    if n == 0:
        pass
    else:
        for h in towerofhanoi(n-1, src, temp, dest):
            yield h
        yield (src, dest)
        for h in towerofhanoi(n-1, temp, dest, src):
            yield h

def towerofhanoi2(n,src,dest,temp):
    if n == 0:
        return

    for h in towerofhanoi2(n-1, src, temp, dest):
        yield h
    yield (src, dest)
    for h in towerofhanoi2(n-1, temp, dest, src):
        yield h

for h in towerofhanoi2(3,1,3,2):
    print h
        
