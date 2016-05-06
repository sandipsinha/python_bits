# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())
d = deque()
for x in xrange(n):
    methods = raw_input()
    method_array = methods.split()
    if len(method_array) > 1:
        method, value = method_array
    else:
        method = method_array[0]
    if method == 'append':
        d.append(value)
    elif method == 'appendleft':
        d.appendleft(value)
    elif method == 'pop':
        d.pop()
    elif method == 'popleft':
        d.popleft()
 

print ' '.join([str(items) for items in list(deque(d))])
