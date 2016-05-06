from collections import defaultdict
from decimal import Decimal
import sys
n=int(raw_input())
k=defaultdict(dict)
for x in range(n):
    m=sys.stdin.readline()
    l=m.strip('\n').split(' ')
    k[l[0]]=[int(item) for item in l[1:]]
name=raw_input()
if name in k:
    print sum(k[name])*1.00
    print len(k[name])

    print Decimal((sum(k[name])*1.00)/len(k[name]))
