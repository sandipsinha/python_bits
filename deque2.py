# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
import sys
num = int(input())




    
runningmax = 0
previousmax = 0

for p in xrange(num):
    
    ind = 'n'
    n = int(input())
    d = deque()
    d.extend([int(items) for items in raw_input().split()])
    while True:
        try:
            n1 = d.pop()
            if n1 > previousmax and previousmax > 0: 
                print 'No'
                ind = 'y'
                break
            n2 = d.popleft()
            if n2 > previousmax and previousmax > 0: 
                print 'No'
                ind = 'y'
                break
            previousmax = min(n1, n2)
          
        except IndexError:
            break

    if ind == 'n':
        print 'yes'
    del d
